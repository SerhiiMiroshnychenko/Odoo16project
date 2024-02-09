from odoo import models, fields


class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    name = fields.Char()
    my_model_id = fields.Many2one('my.model')

    def apply_change_name(self):
        if self.name and self.my_model_id:
            self.my_model_id.write({'name': self.name})
