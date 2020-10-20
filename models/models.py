# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class barcode_article_information(models.Model):
#     _name = 'barcode_article_information.barcode_article_information'
#     _description = 'barcode_article_information.barcode_article_information'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
