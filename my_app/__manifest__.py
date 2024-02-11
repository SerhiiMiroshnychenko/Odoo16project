{
    'name': 'My App',
    'description': '',
    'summary': '',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'website', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_mode_view.xml',
        'views/complex_model_view.xml',
        'views/my_app_menus.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
        'data/ir_cron.xml',
        'data/ir_actions_server.xml',
        'wizard/my_wizard_view.xml',
        'templates/website_templates.xml',
        'reports/sale_order_report.xml',
        'reports/my_report.xml',
    ],
    'assets': {
        'web.assets_backend': [],
        'web.assets_frontend': [],
    },
    'external_dependencies': {
        'python': ['panda', 'numpy']
    }
}