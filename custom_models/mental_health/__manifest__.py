{
    'name': 'Mental Health Notes',
    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/mental_health_security.xml',
        'security/ir.model.access.csv',
        'views/mental_health_notes_views.xml',
        'views/mental_health_notes_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}
