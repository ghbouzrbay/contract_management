from odoo import models, fields, api

class CustomDelivery(models.Model):
    _name = 'custom.delivery'
    _description = 'Bon de Livraison'

    name = fields.Char(string="Référence", required=True, copy=False, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('custom.delivery'))
    order_id = fields.Many2one('custom.order', string="Commande", required=True)
    delivery_line_ids = fields.One2many('custom.delivery.line', 'delivery_id', string="Lignes de livraison")
    date = fields.Datetime(string="Date de livraison", default=fields.Datetime.now)

    @api.model
    def create_delivery_from_order(self, order):
        delivery = self.create({'order_id': order.id})
        for line in order.order_line:
            stock = line.product_id.qty_available
            qty_to_deliver = min(stock, line.quantity)
            self.env['custom.delivery.line'].create({
                'delivery_id': delivery.id,
                'product_id': line.product_id.id,
                'quantity_ordered': line.quantity,
                'quantity_delivered': qty_to_deliver,
            })
        return delivery

class CustomDeliveryLine(models.Model):
    _name = 'custom.delivery.line'
    _description = 'Ligne de Bon de Livraison'

    delivery_id = fields.Many2one('custom.delivery', string="Bon de livraison", required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Produit", required=True)
    quantity_ordered = fields.Float(string="Quantité commandée")
    quantity_delivered = fields.Float(string="Quantité livrée")

