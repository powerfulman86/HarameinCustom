# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class StockBatchProcessor(models.Model):
    _inherit = 'stock.picking.batch'

    def prepare_batch_inventory(self):
        for rec in self:
            if rec.state in ('done', 'cancel'):
                return

            # prepare inventory
            location = rec.picking_ids[0].location_id  # Get location from the first picking
            missing_stock = {}

            # Step 2: Filter only unfinished pickings (exclude 'done' and 'cancel' pickings)
            unfinished_pickings = rec.picking_ids.filtered(lambda p: p.state not in ['done', 'cancel'])

            # Step 2: Check each picking inside the batch
            for picking in unfinished_pickings:
                try:
                    picking.action_assign()
                    for move in picking.move_lines:
                        if move.state not in ['done']:
                            missing_qty = move.product_uom_qty - move.reserved_availability
                            if missing_qty > 0:
                                if move.product_id in missing_stock:
                                    missing_stock[move.product_id] += missing_qty
                                else:
                                    missing_stock[move.product_id] = missing_qty
                except Exception as e:
                    _logger.error(f"Error processing picking {picking.name}: {e}")
                    continue  # Continue to the next picking even if an error occurs

            # Step 3: If stock is missing, create an inventory adjustment
            if missing_stock:
                inventory = self.env['stock.inventory'].create({
                    'name': f'Stock Adjustment for {rec.name}',
                    'is_auto_validate': True,
                    'location_ids': [location.id]
                })

                inventory_lines = []
                for product, missing_qty in missing_stock.items():
                    available_qty_at_location = product.with_context({'location': location.id}).qty_available
                    if available_qty_at_location < 0: available_qty_at_location = 0
                    inventory_lines.append((0, 0, {
                        'inventory_id': inventory.id,
                        'product_id': product.id,
                        'product_qty': available_qty_at_location + missing_qty,
                        'location_id': location.id
                    }))

                inventory.write({'line_ids': inventory_lines})
                inventory.action_start()
                self.env.cr.commit()
