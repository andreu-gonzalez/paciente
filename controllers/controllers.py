# -*- coding: utf-8 -*-
# from odoo import http


# class TareasApp(http.Controller):
#     @http.route('/tareas_app/tareas_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tareas_app/tareas_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tareas_app.listing', {
#             'root': '/tareas_app/tareas_app',
#             'objects': http.request.env['tareas_app.tareas_app'].search([]),
#         })

#     @http.route('/tareas_app/tareas_app/objects/<model("tareas_app.tareas_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tareas_app.object', {
#             'object': obj
#         })
