# -*- coding: utf-8 -*-
# from odoo import http


# class MaquinaCafe(http.Controller):
#     @http.route('/maquina_cafe/maquina_cafe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maquina_cafe/maquina_cafe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('maquina_cafe.listing', {
#             'root': '/maquina_cafe/maquina_cafe',
#             'objects': http.request.env['maquina_cafe.maquina_cafe'].search([]),
#         })

#     @http.route('/maquina_cafe/maquina_cafe/objects/<model("maquina_cafe.maquina_cafe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maquina_cafe.object', {
#             'object': obj
#         })

