{
    'name': 'My App',
    'description': '',
    'summary': '',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_mode_view.xml',
        'views/res_config_settings_views.xml',
        'data/ir_cron.xml',
        'data/ir_actions_server.xml',
        'wizard/my_wizard_view.xml',
        'templates/website_templates.xml',
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