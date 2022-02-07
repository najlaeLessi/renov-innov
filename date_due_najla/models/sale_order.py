# Copyright (C) 2020 - Today GenialSquad Infotech

from odoo import models, api, fields
from datetime import datetime, date, timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def _get_due_date(self):
        due_date = date.today()
        days_conf = self.env['ir.config_parameter'].search(
            [('key', '=', 'sale.days_due_date')])
        if days_conf:
            due_date = due_date + timedelta(days=int(days_conf.value) or 0.0)
        return due_date.strftime('%Y-%m-%d')

    due_date = fields.Date(
        'Due Date', default=_get_due_date, copy=False,
        help='Due date to finish this sale order, the value is calculated '
        'with the today date + days configured in Settings/Sales')