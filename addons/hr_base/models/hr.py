# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    date_of_join = fields.Date('Joining Date')
    date_of_leave =  fields.Date('Leaving Date')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: