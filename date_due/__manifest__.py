# Copyright (C) 2020 - Today GenialSquad Infotech

{
    'name': "Date due pour les bons de commande",
    'version': '13.0.1.0.0',
    'summary': """Create Date due pour les bons de commande""",
    'author': "NJ",
    'company': 'NJ',
    'category': 'Sale',
    'license' : 'OPL-1',
    'depends': ['sale'],
    'data': [
        'data/ir_conf.xml',
        'views/sale_order_view.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
