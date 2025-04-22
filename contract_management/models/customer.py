from odoo import models, fields, api



class Customer(models.Model):
    _name = 'custom.customer'
    _description = 'Customer Model'

    name = fields.Char(string="Nom", required=True)
    address = fields.Text(string="Adresse")
    country_id = fields.Many2one('res.country', string="Pays")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    mobile = fields.Char(string="Mobile")
    active = fields.Boolean(string="Actif", default=True)

    order_ids = fields.One2many('custom.order', 'customer_id', string="Commandes")

    order_count = fields.Integer(string="Nombre de commandes", compute="_compute_order_count")

    @api.depends('order_ids')
    def _compute_order_count(self):
        for record in self:
            record.order_count = len(record.order_ids)
