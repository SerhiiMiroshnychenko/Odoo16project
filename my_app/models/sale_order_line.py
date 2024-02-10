from odoo import fields, models, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_id')
    def _compute_name(self):
        super()._compute_name()
        for line in self.filtered(lambda x: x.product_id):
            line.name = '! ' + line.name
