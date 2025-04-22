class QuotationTemplate(models.Model):
    _name = 'custom.quotation.template'
    _description = "Modèle de devis"

    name = fields.Char(string="Nom du modèle", required=True)
    line_ids = fields.One2many('custom.quotation.template.line', 'template_id', string="Lignes du modèle")


class QuotationTemplateLine(models.Model):
    _name = 'custom.quotation.template.line'
    _description = "Ligne de modèle de devis"

    template_id = fields.Many2one('custom.quotation.template', string="Modèle", ondelete='cascade', required=True)
    product_id = fields.Many2one('product.product', string="Produit", required=True)
    quantity = fields.Float(string="Quantité", default=1.0)

