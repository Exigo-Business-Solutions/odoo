# This code has been written as part of an academic project with the education of
# the student team members being the singular goal and therefore the overarching priority of the project.
# This code should be considered a proof-of-concept rather than a product ready for commercial distribution.
# This code is being provided “as is” with no warranties, express or implied.
#
# Version 0.1 (Pre-Alpha)
{
    'name': 'Mental Health Notes',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
        'icd10',
        'therapists',
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
