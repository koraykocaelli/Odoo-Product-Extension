# -*- coding: utf-8 -*-
{
    'name': 'Odoo Product Extension',
    'author': 'Open Source Contributor',
    'version': '1.0',
    'depends': ['product'],
    'summary': 'Custom fields (Supplier Code, Markup, QR Code) added to product.template model',
    'category': 'Productivity',
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
