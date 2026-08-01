# -*- coding: utf-8 -*-
{
    'name': "Account Enhancement",

    'summary': """
        Account Enhancement""",

    'author': "CubicIt",
    'category': 'Accounting/Accounting',
    'version': '16.0',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['account', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/ir_rule.xml',
        'views/external_layout_template.xml',
        'report/paperformat.xml',
        'report/invoice_two_copies.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
