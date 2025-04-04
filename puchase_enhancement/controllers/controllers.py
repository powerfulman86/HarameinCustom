# -*- coding: utf-8 -*-
# from odoo import http


# class PuchaseEnhancement(http.Controller):
#     @http.route('/puchase_enhancement/puchase_enhancement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/puchase_enhancement/puchase_enhancement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('puchase_enhancement.listing', {
#             'root': '/puchase_enhancement/puchase_enhancement',
#             'objects': http.request.env['puchase_enhancement.puchase_enhancement'].search([]),
#         })

#     @http.route('/puchase_enhancement/puchase_enhancement/objects/<model("puchase_enhancement.puchase_enhancement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('puchase_enhancement.object', {
#             'object': obj
#         })
