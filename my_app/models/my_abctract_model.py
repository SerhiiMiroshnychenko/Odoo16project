from odoo import models


class MyAbstractModel(models.AbstractModel):
    _name = 'my.abstract.model'
    _description = 'My Abstract Model'

    def print_self(self):
        print('Self: %s' % self)
