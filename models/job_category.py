from odoo import models, fields, api

class JobCategory(models.Model):
    _name = 'job.category'
    _description = 'Job Category'

    name = fields.Char(string="Job Title", required=True)
    description = fields.Text(string="Job Description")
    personnel_ids = fields.Many2many('res.partner', 'job_category_res_partner_rel', 'job_category_id', 'partner_id', string="Personnel")
    personnel_count = fields.Integer(string="Number of Personnel", compute='_compute_personnel_count', store=True)

    @api.depends('personnel_ids')
    def _compute_personnel_count(self):
        for record in self:
            record.personnel_count = len(record.personnel_ids)
