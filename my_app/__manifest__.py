{
    'name': 'My App',
    'description': '',
    'summary': '',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_mode_view.xml',
    ],
    'assets': {
        'web.assets_backend': [],
        'web.assets_frontend': [],
    },
    'external_dependencies': {
        'python': ['panda', 'numpy']
    }

}