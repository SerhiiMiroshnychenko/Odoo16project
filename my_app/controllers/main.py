from odoo.http import Controller, route, request


class Main(Controller):

    @route('/my_route', type='http', website=True)
    def my_route(self):
        values = {
            'name': 'Serhii',
            'city': 'Mariupol',
            'age': 42,
            'alist': [1, 2, 3, 5, 8]
        }
        return request.render('my_app.my_route_template', values)
