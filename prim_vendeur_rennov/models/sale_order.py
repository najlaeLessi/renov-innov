from odoo import models, api, fields, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    primev = fields.Float('mtn ht par vendeur',store=True)
    nbrprimev = fields.Float('nbre des vendeurs',store=True)


    @api.onchange('amount_untaxed','x_studio_vendeur_1','x_studio_vendeur_2','x_studio_vendeur_3')
    def on_change_vendeur(self):
        for record in self:
            #record.primev=0
            if record.x_studio_vendeur_1:
                record.primev=record.amount_untaxed
                record.nbrprimev=1
            if record.x_studio_vendeur_1 and record.x_studio_vendeur_2:
                record.primev=record.amount_untaxed/2
                record.nbrprimev=2
            if record.x_studio_vendeur_1 and record.x_studio_vendeur_2  and record.x_studio_vendeur_3:
                record.primev=record.amount_untaxed/3
                record.nbrprimev=3





#    @api.depends('mntF')
#    def _on_change_credit(self):
#        for record in self:
#            if record.mntF:
#                if record.mntF > 0 and record.amount_total > record.mntF:
#                    record.mntFchar='p p'
#                if record.amount_total == record.mntF:
#                    record.mntFchar='n p'
#            if record.mntF==0:
#                record.mtnFchar='c p'                                                