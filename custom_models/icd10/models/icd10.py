# This code has been written as part of an academic project with the education of
# the student team members being the singular goal and therefore the overarching priority of the project.
# This code should be considered a proof-of-concept rather than a product ready for commercial distribution.
# This code is being provided “as is” with no warranties, express or implied.
#
# Version 0.1 (Pre-Alpha)
from odoo import fields, models


class ICD10Codes(models.Model):
    _name = "icd10"
    _description = "A module to store ICD10 codes."
    _rec_name = "icd10_name"

    icd10_id = fields.Text()
    icd10_name = fields.Text()
