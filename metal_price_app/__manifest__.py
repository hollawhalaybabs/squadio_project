# -*- coding: utf-8 -*-
#############################################################################
#
#############################################################################

{
    'name': 'Metal Price Module',
    'version': '14.0.1.0.0',
    'category': 'Purchase',
    'summary': """Update Metal Price""",
    'author': 'Olawale Babalola',
    'website': "https://www.novussolutions.com.ng",
    'company': 'Novus Solutions',
    'maintainer': 'Novus Solutions',
    'depends': ['account','base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/metal_price_view.xml',
        'views/account_move_inherit_view.xml',
        'views/partner_inherit.xml'
        
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
