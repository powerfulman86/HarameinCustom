# -*- coding: utf-8 -*-
{
    'name': "Purchase Enhancement",

    'summary': """
        Purchase Enhancement""",

    'author': "CubicIt",
    'category': 'Inventory/Purchase',
    'version': '16.0',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['purchase'],

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
