# This code has been written as part of an academic project with the education of
# the student team members being the singular goal and therefore the overarching priority of the project.
# This code should be considered a proof-of-concept rather than a product ready for commercial distribution.
# This code is being provided “as is” with no warranties, express or implied.
#
# Version 0.1 (Pre-Alpha)
{
    'name': 'Therapist Assignment',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/therapists_security.xml',
        'security/ir.model.access.csv',
        'views/therapist_assignment_views.xml',
        'views/therapist_assignment_menus.xml',
    ],
    'installable': True,
    'auto_install': True
}
