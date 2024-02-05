from odoo import fields, models


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char()
    long_text = fields.Text()
    an_int = fields.Integer()
    a_float = fields.Float()
    a_bool = fields.Boolean()
    a_date = fields.Date()
    a_datetime = fields.Datetime()
    a_selection = fields.Selection([('option1', 'Option1'), ('option2', 'Option2')])
    a_html = fields.Html()
    a_binary = fields.Binary()
    an_image = fields.Image()
