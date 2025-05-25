from odoo import models, fields, api
import qrcode
from io import BytesIO
import base64

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_code = fields.Char(string="Supplier Code")
    markup = fields.Float(string="Markup")
    qrcode = fields.Binary(string="QR Code", compute="_compute_qrcode", store=True)

    @api.depends('supplier_code')
    def _compute_qrcode(self):
        for record in self:
            if record.supplier_code:
                qr = qrcode.make(record.supplier_code)
                buffer = BytesIO()
                qr.save(buffer, format="PNG")
                record.qrcode = base64.b64encode(buffer.getvalue())
            else:
                record.qrcode = False

    @api.constrains('markup')
    def _check_markup(self):
        for record in self:
            if record.markup < 0:
                raise ValueError("Markup must be zero or positive!")
