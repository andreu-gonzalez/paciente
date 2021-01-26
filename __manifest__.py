# -*- coding: utf-8 -*-
{
    'name': "Gestor de pacientes",

    'summary': """
        Aplicación para la gestión de consultas medicas""",

    'description': """
        Aplicación para la gestión de tareas simple
    """,

    'author': "Andreu gonzalez",
    'website': "http://www..com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pacientes_view.xml',
        'views/visitas_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
