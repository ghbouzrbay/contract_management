from odoo import http
from odoo.http import request
import json

class CustomOrderController(http.Controller):

    @http.route('/custom/orders', auth='public', type='json', methods=['GET'], csrf=False)
    def get_orders(self):
        orders = request.env['custom.order'].sudo().search([], limit=10)
        result = []
        for order in orders:
            result.append({
                'id': order.id,
                'name': order.name,
                'customer': order.customer_id.name,
                'date_order': str(order.date_order),
                'amount_total': order.amount_total,
            })
        return result

    @http.route('/custom/order/<int:order_id>', auth='public', type='json', methods=['GET'], csrf=False)
    def get_order_by_id(self, order_id):
        order = request.env['custom.order'].sudo().browse(order_id)
        if not order.exists():
            return {'error': 'Commande non trouvée'}
        
        return {
            'id': order.id,
            'name': order.name,
            'customer': order.customer_id.name,
            'date_order': str(order.date_order),
            'amount_total': order.amount_total,
            'lines': [
                {
                    'product': line.product_id.name,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'price_total': line.price_total,
                } for line in order.order_line
            ]
        }

