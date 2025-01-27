# This code has been written as part of an academic project with the education of
# the student team members being the singular goal and therefore the overarching priority of the project.
# This code should be considered a proof-of-concept rather than a product ready for commercial distribution.
# This code is being provided “as is” with no warranties, express or implied.
#
# Version 0.1 (Pre-Alpha)
from odoo import fields, models


class MentalHealthNotes(models.Model):
    _name = "mental_health.notes"
    _description = "A model to be used to write mental health notes"

    client_id = fields.Many2one(comodel_name='res.users', required=True, copy=True,
                             domain=lambda self: [('id', 'in', self.env["therapists"].search(
                                 [('therapist', '=', self.env.uid)]).assigned_clients.ids)])
    mode_of_therapy = fields.Selection(string='Mode of Therapy', required=True,
                                       selection=[('in_person', 'In Person'),
                                                  ('by_phone', 'By Phone'),
                                                  ('video_conference_online', 'Video Conference Online'),
                                                  ('email', 'Email'),
                                                  ('text', 'Text')],
                                       default='in_person',
                                       help='Select the mode of therapy.')

    date = fields.Date(string='Date Recorded', required=True, default=lambda self: fields.Date.today(), copy=False,
                       readonly=True)
    arrival_status = fields.Selection(string='Arrival Status', required=True,
                                      selection=[('on_time', 'On Time'),
                                                 ('late', 'Late'),
                                                 ('no_show', 'No Show'),
                                                 ('cancelled', 'Cancelled')],
                                      default='on_time',
                                      help='Select the arrival status of the client.')
    service_type = fields.Selection(string='Service Provided', required=True,
                                    selection=[('intake', 'Intake'),
                                               ('individual_therapy', 'Individual Therapy')],
                                    default='individual_therapy',
                                    help='Select the type of service provided.')
    icd10_code = fields.Many2one(string='ICD10 Code', comodel_name='icd10', required=False, copy=False)
    description = fields.Text(string='Meeting Notes', copy=False)
    thought_process = fields.Selection(string='Thought Process', required=True, copy=False,
                                       selection=[('normal', 'Normal'),
                                                  ('lessened_awareness', 'Lessened awareness'),
                                                  ('memory_deficiency', 'Memory deficiency'),
                                                  ('disoriented', 'Disoriented'),
                                                  ('disorganized', 'Disorganized'),
                                                  ('vigilant', 'Vigilant'),
                                                  ('delusional', 'Delusional'),
                                                  ('hallucinating', 'Hallucinating')],
                                       default='normal',
                                       help='Select the thought process of the client.')
    suicidal_homicidal = fields.Selection(string='Suicidal/Homicidal', required=True, copy=False,
                                          selection=[('none', 'None'),
                                                     ('ideation_only', 'Ideation only'),
                                                     ('threat', 'Threat'),
                                                     ('gesture', 'Gesture'),
                                                     ('rehearsal', 'Rehearsal'),
                                                     ('attempt', 'Attempt'),
                                                     ('plan', 'Plan')],
                                          default='none',
                                          help='Is the client suicidal or homicidal?')
    insight = fields.Selection(string='Insight', required=True, copy=False,
                               selection=[('poor', 'Poor'),
                                          ('limited', 'Limited'),
                                          ('fair', 'Fair'),
                                          ('good', 'Good')],
                               default='good',
                               help='Select the level of insight of the client.')
    participation = fields.Selection(string='Participation Level', required=True, copy=False,
                                     selection=[('active', 'Active'),
                                                ('variable', 'Variable'),
                                                ('responsive_only', 'Responsive only'),
                                                ('minimal', 'Minimal'),
                                                ('resistant', 'Resistant')],
                                     default='active',
                                     help='Select the participation level of the client.')
    motivation = fields.Selection(string='Motivation', required=True, copy=False,
                                  selection=[('low', 'Low'),
                                             ('moderate', 'Moderate'),
                                             ('high', 'High')],
                                  default='high',
                                  help='Select the level of motivation of the client.')
    affect = fields.Selection(string='Affect', required=True, copy=False,
                              selection=[('normal', 'Normal'),
                                         ('slumped', 'Slumped'),
                                         ('slowed', 'Slowed'),
                                         ('confident', 'Confident'),
                                         ('energetic', 'Energetic'),
                                         ('nervous', 'Nervous'),
                                         ('fidgety', 'Fidgety')],
                              default='normal',
                              help='Select the affect of the client')
    symptom_change = fields.Selection(string='Change in Symptom Severity', required=True, copy=False,
                                      selection=[('resolved', 'Resolved'),
                                                 ('much_improved', 'Much improved'),
                                                 ('less_but_still_observable', 'Less but still observable.'),
                                                 ('same', 'Same'),
                                                 ('more_severe', 'More severe')],
                                      default='same',
                                      help='Has there been any change in the symptom severity of the client?')
    diagnosis_selection = fields.Selection(string='Diagnosis', required=True, copy=False,
                                           selection=[('no_change', 'No change'),
                                                      ('change', 'Change'),
                                                      ('additional', 'Additional')],
                                           default='no_change',
                                           help='Has there been a change in the diagnosis of the client?')
    judgment = fields.Selection(string='Judgment', required=True, copy=False,
                                selection=[('poor', 'Poor'),
                                           ('limited', 'Limited'),
                                           ('fair', 'Fair'),
                                           ('good', 'Good')],
                                default='good',
                                help='Select the judgment level of the client.')
    eating = fields.Selection(string='Eating', required=True, copy=False,
                              selection=[('normal', 'Normal'),
                                         ('more', 'More'),
                                         ('binging', 'Binging'),
                                         ('less', 'Less'),
                                         ('starving', 'Starving'),
                                         ('over_exercising', 'Over exercising')],
                              default='normal',
                              help='Select the eating patterns of the client.')
    sleep_quality = fields.Selection(string='Sleep Quality', required=True, copy=False,
                                     selection=[('normal', 'Normal'),
                                                ('restless/broken', 'Restless/broken'),
                                                ('insomnia', 'Insomnia'),
                                                ('nightmares', 'Nightmares'),
                                                ('oversleeps', 'Oversleeps')],
                                     default='normal',
                                     help='Select the sleep quality of the client.')
    mood = fields.Selection(string='Mood', required=True, copy=False,
                            selection=[('normal', 'Normal'),
                                       ('anxious', 'Anxious'),
                                       ('depressed', 'Depressed'),
                                       ('angry', 'Angry'),
                                       ('euphoric', 'Euphoric')],
                            default='normal',
                            help='Select the mood of the client.')
    homework = fields.Text(string='Homework Assignment')
    therapist_id = fields.Text(string="Therapist Id", invisible=True, default=lambda self: self.env.uid, required=True,
                               copy=False)

    search_ids = fields.Char(compute="_compute_search_ids", search='_search_ids_search')

    def _compute_search_ids(self):
        for note in self:
            note.search_ids = (note.therapist_id == self.env.uid) or (note.client.id == self.env.uid)

    def _search_ids_search(self, operator, operand):
        obj = self.env['mental_health.notes'].search(
            ['|', ('therapist_id', '=', self.env.uid), ('client', '=', self.env.uid)]).ids
        return [('id', 'in', obj)]
