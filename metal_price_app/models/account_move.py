from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"
    
    metal_price = fields.Float(string="Metal Price",compute='_get_metal_price', store=True)
    
    @api.depends('metal_price')
    def _get_metal_price(self):
        price_obj = self.env['metal.price.wizard'].search([('date', '=', fields.Date.today())], limit=1)
        if price_obj:
            self.metal_price = price_obj.metal_price         
        else:
            price_obj.create({
                'metal_price': self.metal_price,
                'date': fields.Date.today(),
            })
        return True
            
    # def write(self, vals):
    #     res = super(AccountMove, self).write(vals)
    #     self._get_metal_price()
    #     return res
            
class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    
    @api.onchange("product_id")          
    def _get_unit_price(self):
        for rec in self:
            uom = self.product_uom_category_id.name
            if uom == "Weight":
                self.product_id.lst_price = rec.move_id.metal_price
                self.price_unit = rec.move_id.metal_price
            else:
                pass
            #   raise ValidationError('product UoM is not in weight')
            
            
    
        
           
                

                
    
        