#-*- coding: utf-8 -*-
from odoo import fields, models, api

class Product(models.Model):
    _inherit = 'product.product'
    availablity = fields.Boolean(compute='compute_availablity', string=" Product Availablity")

    @api.depends('qty_available')
    def compute_availablity(self):
        quantity = self.qty_available
        if (quantity <= 0):
            self.availablity = False
        else:
            self.availablity = True
