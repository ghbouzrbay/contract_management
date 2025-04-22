from odoo import models, fields, api
import plotly.express as px
import logging
_logger = logging.getLogger(__name__)



class Order(models.Model):
    _name = 'custom.order'
    _description = 'Order Model'

    name = fields.Char(string="Référence Commande", required=True, copy=False,
                       default=lambda self: self.env['ir.sequence'].next_by_code('custom.order'))
    customer_id = fields.Many2one('custom.customer', string="Client", required=True)
    address = fields.Text(string="Adresse Client", related='customer_id.address', store=True)
    date_order = fields.Date(string="Date de commande", default=fields.Date.today)

    order_line = fields.One2many('custom.order.line', 'order_id', string="Lignes de commande")

    amount_total = fields.Monetary(string="Total", compute="_compute_amount_total", store=True,
                                   currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Devise', required=True,
                                  default=lambda self: self.env.company.currency_id)

    pricelist_id = fields.Many2one('product.pricelist', string="Liste de prix")
    payment_term_id = fields.Many2one('account.payment.term', string="Conditions de paiement")


    user_id = fields.Many2one(
        'res.users',
        string="Vendeur",
        default=lambda self: self.env.user,
        readonly=True
    )
    team_id = fields.Many2one('crm.team', string="Equipe Commerciale")
    tag_ids = fields.Many2many('crm.tags', string="Etiquettes")
    original = fields.Char(string="Document Original")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunité")
    medium_id = fields.Many2one('utm.medium', string="Moyen")
    source_id = fields.Many2one('utm.source', string="Source")
    costumer_reference = fields.Char(string="Réference Client")


    @api.depends('order_line.price_total')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(record.order_line.mapped('price_total'))


    @api.model
    def cron_check_orders(self):
        orders = self.search([('date_order', '<', fields.Date.today())])
        for order in orders:
            _logger.info(f"Commande à vérifier : {order.name} du {order.date_order}")



    # Méthode pour récupérer les valeurs du rapport
        @api.model
        def get_report_values(self, docids, data=None):
            docs = self.browse(docids)  # Récupère les commandes par leurs IDs
            return {
                'doc_ids': docids,
                'doc_model': 'custom.order',
                'docs': docs,  # Assurez-vous que vous passez 'docs' et non 'doc'
            }


    #Le champ + La relation de module de commande et le modèle de devis
    template_id = fields.Many2one('custom.quotation.template', string="Modèle de devis")

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            lines = []
            for template_line in self.template_id.line_ids:
                lines.append((0, 0, {
                    'product_id': template_line.product_id.id,
                    'quantity': template_line.quantity,
                }))
            self.order_line = lines

    def generate_graph(self, sales_data):
        # Extrait les données
        customers = [data['customer_id'][1] for data in sales_data]
        totals = [data['amount_total'] for data in sales_data]

        # Crée un graphique à barres avec Plotly
        fig = px.bar(x=customers, y=totals, labels={'x': 'Client', 'y': 'Total des ventes'})
        return fig.to_html()



class OrderLine(models.Model):
    _name = 'custom.order.line'
    _description = 'Order Line Model'

    # le premier onglet "lignes de commande"

    order_id = fields.Many2one('custom.order', string="Commande", required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Produit", required=True)
    quantity = fields.Float(string="Quantité", default=1.0)
    price_unit = fields.Float(string="Prix Unitaire", related='product_id.list_price', store=True)
    currency_id = fields.Many2one('res.currency', string='Devise', required=True,
                                  default=lambda self: self.env.company.currency_id)
    price_total = fields.Monetary(string="Total", compute="_compute_price_total", store=True, currency_field='currency_id')

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for record in self:
            record.price_total = record.quantity * record.price_unit
