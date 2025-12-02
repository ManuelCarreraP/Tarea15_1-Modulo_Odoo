# -*- coding: utf-8 -*-
{
    'name': "Maquina Cafe",
    'summary': "Modulo para calcular café según nivel de sueño",
    'description': """
        Recomienda bebidas según el nivel de sueño:
        • 1 a 3 → Café con leche
        • 4 a 6 → Café solo largo
        • 7 a 9 → Café solo larguísimo
        • 10 → Inyección de adrenalina
    """,
    'author': "Manuel Carrera",
    'website': "https://www.manuelcarrera.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}