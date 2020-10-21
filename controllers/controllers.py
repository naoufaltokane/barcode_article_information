# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.stock_barcode.controllers.main import StockBarcodeController

class StockBarcodeController(StockBarcodeController):

    @http.route('/stock_barcode/scan_from_main_menu', type='json', auth='user')
    def main_menu(self, barcode, **kw):
        """ Receive a barcode scanned from the main menu and return the appropriate
            action (open an existing / new picking) or warning.
        """
        ret_open_picking = self.try_open_picking(barcode)
        if ret_open_picking:
            return ret_open_picking

        ret_open_picking_type = self.try_open_picking_type(barcode)
        if ret_open_picking_type:
            return ret_open_picking_type

        if request.env.user.has_group('stock.group_stock_multi_locations'):
            ret_new_internal_picking = self.try_new_internal_picking(barcode)
            if ret_new_internal_picking:
                return ret_new_internal_picking

        ret_show_product = self.try_show_product(barcode)
        if ret_show_product:
            return ret_show_product

        if request.env.user.has_group('stock.group_stock_multi_locations'):
            return {'warning': _('No picking or location corresponding to barcode %(barcode)s') % {'barcode': barcode}}
        else:
            return {'warning': _('No picking corresponding to barcode %(barcode)s') % {'barcode': barcode}}

    def try_show_product(self, barcode):
        corresponding_product = request.env['product.product'].search([('barcode', '=', barcode),], limit=1)
        if corresponding_product:
            view_id = request.env.ref('product.product_template_form_view').id
            return {
                'action': {
                    'name': _('open product form'),
                    'res_model': 'product.product',
                    'view_mode': 'form',
                    'view_id': view_id,
                    'views': [(view_id, 'form')],
                    'type': 'ir.actions.act_window',
                    'res_id': corresponding_product.id,
                }
            }