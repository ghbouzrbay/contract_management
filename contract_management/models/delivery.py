from odoo import models, fields, api

class CustomDelivery(models.Model):
    _name = 'custom.delivery'
    _description = 'Livraison'

    name = fields.Char(string="Référence", required=True, copy=False, readonly=True, default='Nouveau')
    order_id = fields.Many2one('custom.order', string="Commande liée", required=True)
    delivery_date = fields.Date(string="Date de livraison", required=True)
    delivered = fields.Boolean(string="Livré", default=False)
    note = fields.Text(string="Note")

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouveau') == 'Nouveau':
            vals['name'] = self.env['ir.sequence'].next_by_code('custom.delivery') or 'Nouveau'
        return super().create(vals)

