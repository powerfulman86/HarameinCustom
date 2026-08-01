# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class puchase_enhancement(models.Model):
#     _name = 'puchase_enhancement.puchase_enhancement'
#     _description = 'puchase_enhancement.puchase_enhancement'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
