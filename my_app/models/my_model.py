from odoo import fields, models, api
from odoo.exceptions import UserError


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'
    _inherit = ['my.abstract.model', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    code = fields.Char(compute='_compute_code', search='_search_code')
    long_text = fields.Text()
    an_int = fields.Integer()
    a_float = fields.Float(digits=(10, 3))
    a_bool = fields.Boolean(compute='_compute_a_bool', store=True)
    a_date = fields.Date()
    a_datetime = fields.Datetime()
    a_selection = fields.Selection([('option1', 'Option1'), ('option2', 'Option2')])
    a_html = fields.Html()
    a_binary = fields.Binary(attachment=True)  # Зберігається в ir.attachment
    an_image = fields.Image(attachment=False)  # Зберігається в my.model

    new_model_id = fields.Many2one('new.model')
    new_model_m2m_ids = fields.Many2many('new.model', string='New Models')
    new_model_o2m_ids = fields.One2many('new.model', 'my_model_id')
    contact_id = fields.Many2one('res.partner')
    has_especially_contact = fields.Boolean(compute='_compute_has_especially_contact', readonly=True)

    def action_print_true(self):
        print('True %s %d' % (self, self.id))

    def action_sorted_by_name(self):
        my_models = self.env['my.model'].search([]).sorted('name', reverse=True).mapped('name')
        print(f"{my_models = }")

    def action_filtered_by_bool(self):
        my_models = self.env['my.model'].search([]).filtered(lambda x: x.a_bool is True).mapped('name')
        print(f"{my_models = }")

    def action_change_name(self):
        action = {
            'type': 'ir.actions.act_window',
            'name': 'My Wizard Popup',
            'res_model': 'my.wizard',
            'target': 'new',
            'view_mode': 'form',
            'context': {
                'default_my_model_id': self.id
            }
        }
        return action

    @api.onchange('name')  # Не спрацьовує, якщо змінюється через Wizard
    def _onchange_name(self):
        if self.name:
            self.an_int = len(self.name)

    @api.depends('name')  # Спрацьовує, якщо змінюється через Wizard
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

    def _add_to_float(self):
        for m in self.search([]):  # Якщо в тому ж самому модулі
            m.a_float += 1.0

    def decrease_float_by_1(self):
        for m in self.browse(self.env.context.get('active_ids')):
            m.a_float -= 1.0

    def _compute_code(self):
        for rec in self:
            if name := rec.name:
                rec.code = name[0] + str(len(name)) + name[-1]

    def _search_code(self, operator, value):  # Тепер працює! :-)
        field_ids = self.search([]).filtered(lambda x: value in x.code)
        return [('id', 'in', [x for x in field_ids.ids] if field_ids else False)]

    @api.depends('contact_id')
    def _compute_has_especially_contact(self):
        especially_contact_id = int(self.env['ir.config_parameter'].sudo().get_param('my_app.especially_contact_id'))
        for rec in self:
            if rec.contact_id and rec.contact_id.id == especially_contact_id:
                rec.has_especially_contact = True
            else:
                rec.has_especially_contact = False

    def get_another_var(self):
        return f'{self.code} {self.name}'


class NewModel(models.Model):
    _name = 'new.model'
    _description = 'New Model'

    name = fields.Char()
    my_model_id = fields.Many2one('my.model')
