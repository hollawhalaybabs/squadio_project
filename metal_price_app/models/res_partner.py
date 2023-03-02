from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = 'res.partner'
    
    total_weight_invoiced = fields.Monetary(compute='_invoice_weight_total', string="Total Weight Invoiced")
    
    def _invoice_weight_total(self):
        self.total_weight_invoiced = 0
        if not self.ids:
            return True

        all_partners_and_children = {}
        all_partner_ids = []
        for partner in self.filtered('id'):
            # price_total is in the company currency
            all_partners_and_children[partner] = self.with_context(active_test=False).search([('id', 'child_of', partner.id)]).ids
            all_partner_ids += all_partners_and_children[partner]

        domain = [
            ('partner_id', 'in', all_partner_ids),
            ('state', 'not in', ['draft', 'cancel']),
            ('move_type', 'in', ('out_invoice', 'out_refund')),
        ]
        quantity_totals = self.env['account.invoice.report'].read_group(domain, ['quantity'], ['partner_id'])
        for partner, child_ids in all_partners_and_children.items():
            partner.total_weight_invoiced = sum(qty['quantity'] for qty in quantity_totals if qty['partner_id'][0] in child_ids)