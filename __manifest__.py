# -*- coding: utf-8 -*-
{
    'name': "Website custom",
    'summary': "Customizations for Odoo website",
    'description': "Customizations for Odoo website",
    'author': "Parfait BENE MANGA",
    'website': "http://www.parfaitbene.com",
    'category': 'Website',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        "views/webclient_templates.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
