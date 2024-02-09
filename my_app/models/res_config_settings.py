from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    especially_contact_id = fields.Many2one(
        'res.partner',
        config_parameter='my_app.especially_contact_id')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'my_app.especially_contact_id', str(self.especially_contact_id.id))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            especially_contact_id=int(params.get_param('my_app.especially_contact_id'))
        )
        return res
