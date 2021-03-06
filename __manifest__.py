#-*- coding: utf-8 -*-
{
    'name': "Credit Schemes",
    'summary': """
        module for credit schemes
    """,
    'description': """
        module for credit schemes
    """,
    'author': "Francisco Castillo Moo",
    'website': "",
    'version': '0.1',
    "license": "OPL-1",
    'depends': [
        'base',
        'contract',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/credit_schemes_views.xml',
        'views/contract_contract_view_inherit.xml',
        'views/res_partner_view_inherit.xml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

