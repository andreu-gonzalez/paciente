from odoo import models, fields, api
from random import choice
from datetime import datetime
from odoo.exceptions import ValidationError

class visitas_model(models.Model):
    _name = 'medico.visitas_model'
    _description = 'medico.visitas_model'
    
    nombre = fields.Many2one("medico.pacientes_model","nombre") 
    fecha= fields.Datetime()
    detalle = fields.Html(string="detalle", required=True, index=True,help="nombre del paciente") 
    paciente = fields.Many2one("medico.pacientes_model")