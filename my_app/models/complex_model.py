from odoo import fields, models, api


class ComplexModel(models.Model):
    _name = 'complex.model'
    _inherits = {'res.partner': 'partner_id', 'my.model': 'my_model_id'}

    title = fields.Char(compute='_compute_title')
    partner_id = fields.Many2one('res.partner')
    my_model_id = fields.Many2one('my.model')

    def _compute_title(self):
        for rec in self:
            if rec.partner_id.name and rec.my_model_id.an_int:
                rec.title = f'{rec.partner_id.name}-{rec.my_model_id.an_int}'
            else:
                rec.title = f'Name-{rec.id}'
