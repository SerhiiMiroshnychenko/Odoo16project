from odoo import fields, models, api
from odoo.exceptions import UserError


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char()
    long_text = fields.Text()
    an_int = fields.Integer()
    a_float = fields.Float()
    a_bool = fields.Boolean(compute='_compute_a_bool', store=True)
    a_date = fields.Date()
    a_datetime = fields.Datetime()
    a_selection = fields.Selection([('option1', 'Option1'), ('option2', 'Option2')])
    a_html = fields.Html()
    a_binary = fields.Binary()
    an_image = fields.Image()

    new_model_id = fields.Many2one('new.model')
    new_model_m2m_ids = fields.Many2many('new.model', string='New Models')
    new_model_o2m_ids = fields.One2many('new.model', 'my_model_id')

    def action_print_true(self):
        print('True %s %d' % (self, self.id))

    def action_sorted_by_name(self):
        my_models = self.env['my.model'].search([]).sorted('name', reverse=True).mapped('name')
        print(f"{my_models = }")

    def action_filtered_by_bool(self):
        my_models = self.env['my.model'].search([]).filtered(lambda x: x.a_bool is True).mapped('name')
        print(f"{my_models = }")

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.an_int = len(self.name)

    @api.depends('name')
    def _compute_a_bool(self):
        for rec in self:
            if rec.name and len(rec.name) > 3:
                rec.a_bool = True
            else:
                rec.a_bool = False

    @api.constrains('name')
    def _check_name_smaller_10(self):
        for rec in self:
            if rec.name and len(rec.name) >= 10:
                raise UserError("Name can't be longer then 10 chars.")


class NewModel(models.Model):
    _name = 'new.model'
    _description = 'New Model'

    name = fields.Char()
    my_model_id = fields.Many2one('my.model')
