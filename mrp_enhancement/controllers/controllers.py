# -*- coding: utf-8 -*-
# from odoo import http


# class MrpEnhancement(http.Controller):
#     @http.route('/mrp_enhancement/mrp_enhancement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_enhancement/mrp_enhancement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_enhancement.listing', {
#             'root': '/mrp_enhancement/mrp_enhancement',
#             'objects': http.request.env['mrp_enhancement.mrp_enhancement'].search([]),
#         })

#     @http.route('/mrp_enhancement/mrp_enhancement/objects/<model("mrp_enhancement.mrp_enhancement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_enhancement.object', {
#             'object': obj
#         })
