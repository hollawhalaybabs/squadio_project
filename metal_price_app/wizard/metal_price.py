from datetime import datetime, timedelta
from odoo import fields, models, _
from odoo.exceptions import ValidationError, UserError, RedirectWarning

class MetalPriceWizard(models.Model):
    _name = 'metal.price.wizard'
    _description  = "Wizard to enable adding new metal price"
    _rec_name = "metal_price"
    _order= "id desc"
    
    metal_price = fields.Float(string="Metal Price", digits='Product Price')
    date = fields.Date(string="Date", default=lambda self: fields.Date.today())
    
    
    def post_action(self): 
        return{'type': 'ir.actions.act_window_close'}