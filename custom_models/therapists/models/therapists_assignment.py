from odoo import fields, models


class TherapistAssignments(models.Model):
    _name = "therapists"
    _description = "A model to be used to assign therapists to clients"
    _rec_name = 'therapist'

    therapist = fields.Many2one('res.users', string="Therapist",
                                # domain=lambda self: [("group_ids", "=",
                                #                       self.env.ref(
                                #                           "mental_health.group_mental_health_therapist").id)],
                                required=True)

    assigned_clients = fields.Many2many('res.users', 'assigned_clients_rel', 'client_id', string="Assigned Clients",
                                        # domain=lambda self: [("group_ids", "=",
                                        #                       self.env.ref(
                                        #                           "mental_health.group_mental_health_user").id)],
                                        required=True)
