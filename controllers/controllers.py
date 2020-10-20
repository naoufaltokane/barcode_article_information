# -*- coding: utf-8 -*-
# from odoo import http


# class BarcodeArticleInformation(http.Controller):
#     @http.route('/barcode_article_information/barcode_article_information/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barcode_article_information/barcode_article_information/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('barcode_article_information.listing', {
#             'root': '/barcode_article_information/barcode_article_information',
#             'objects': http.request.env['barcode_article_information.barcode_article_information'].search([]),
#         })

#     @http.route('/barcode_article_information/barcode_article_information/objects/<model("barcode_article_information.barcode_article_information"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barcode_article_information.object', {
#             'object': obj
#         })
