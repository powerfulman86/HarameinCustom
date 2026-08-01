# -*- coding: utf-8 -*-

from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_invoice_previous_balance(self):
        """Return the customer's open balance before the current invoice.

        The amount is expressed in the current invoice company currency and
        includes posted customer invoices/refunds dated before this invoice.
        """
        self.ensure_one()
        if self.move_type not in ("out_invoice", "out_refund", "out_receipt"):
            return 0.0

        partner = self.commercial_partner_id
        if not partner:
            return 0.0

        domain = [
            ("id", "!=", self.id),
            ("state", "=", "posted"),
            ("company_id", "=", self.company_id.id),
            ("commercial_partner_id", "=", partner.id),
            ("move_type", "in", ("out_invoice", "out_refund", "out_receipt")),
        ]
        if self.invoice_date:
            domain += [
                "|",
                ("invoice_date", "<", self.invoice_date),
                "&",
                ("invoice_date", "=", self.invoice_date),
                ("id", "<", self.id),
            ]

        moves = self.env["account.move"].search(domain)
        return sum(moves.mapped("amount_residual_signed"))

    def _get_invoice_paid_amount(self):
        """Return the amount already paid/settled on this invoice."""
        self.ensure_one()
        return self.amount_total_signed - self.amount_residual_signed
