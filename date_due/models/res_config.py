# Copyright (C) 2020 - Today GenialSquad Infotech

from odoo import api, fields, models


class SaleConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    days_due_date_sale = fields.Integer(
        'Days to due date',
        help='Number of days that will add to the date when is created the '
        'sale order as due date.')

 
    def set_days_due_date(self):
        param = self.env['ir.config_parameter'].search(
            [('key', '=', 'sale.days_due_date')])
        if param:
            param.write({'value': self.days_due_date_sale})
        return True


    def get_default_days_due_date_sale(self):
        days = self.env['ir.config_parameter'].search(
            [('key', '=', 'sale.days_due_date')])
        return {'days_due_date_sale': int(days.value) or 0.0}
