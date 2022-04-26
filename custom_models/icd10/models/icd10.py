from odoo import fields, models


class ICD10Codes(models.Model):
    _name = "icd10"
    _description = "A module to store ICD10 codes."
    _rec_name = "icd10_name"

    icd10_id = fields.Text()
    icd10_name = fields.Text()

