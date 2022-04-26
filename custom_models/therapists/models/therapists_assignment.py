from odoo import fields, models


class TherapistAssignments(models.Model):
    _name = "therapists"
    _description = "A model to be used to assign therapists to clients"
    _rec_name = 'therapist'

    therapist = fields.Many2one('res.users', string="Therapist",
                                # domain=lambda self: [("group_ids", "=",
                                #                       self.env.ref(
                                #                           "mental_health.group_mental_health_therapist").id)],
                                required=True, domain=lambda self: [('groups_id', '=', self.env.ref('mental_health.group_mental_health_therapist').id)])

    assigned_clients = fields.Many2many('res.users', 'assigned_clients_rel', 'client_id', string="Assigned Clients",
                                        # domain=lambda self: [("group_ids", "=",
                                        #                       self.env.ref(
                                        #                           "mental_health.group_mental_health_user").id)],
                                        required=True, domain=lambda self: [
            ('groups_id', '=', self.env.ref('mental_health.group_mental_health_user').id)])

    search_ids = fields.Char(compute="_compute_search_ids", search="_search_ids_search")

    def _compute_search_ids(self):
        for therapists in self:
            therapists.search_ids = (therapists.therapist == self.env.uid) or self.env['res.users'].browse(self.env.uid).has_group('therapists.group_therapists_admin')

    def _search_ids_search(self, operator, operand):

        #Allow therapists to view their own assignments
        obj = self.env['therapists'].search(
            [('therapist', '=', self.env.uid)]).ids

        #Allow admins to view all records
        if self.env['res.users'].browse(self.env.uid).has_group('therapists.group_therapists_admin'):
            obj = self.env['therapists'].search([]).ids

        return [('id', 'in', obj)]
