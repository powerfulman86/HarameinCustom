# -*- coding: utf-8 -*-
{
    'name': "Stock Enhancement",

    'summary': """
        Stock Enhancement""",

    'author': "CubicIt",
    'category': 'Inventory/Inventory',
    'version': '16.0',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir_rule.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
