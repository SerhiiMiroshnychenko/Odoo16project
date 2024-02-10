from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_date = fields.Date()
    custom_char = fields.Char()
    my_model_id = fields.Many2one('my.model')
