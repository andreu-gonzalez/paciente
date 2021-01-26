# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from datetime import datetime
from odoo.exceptions import ValidationError
from datetime import date
class pacientes_model(models.Model):
    _name = 'medico.pacientes_model'
    _description = 'medico.pacientes_model'

    _rec_name="nombre"
    dni = fields.Char(string="DNI",required=True,index=True,help="El dni del paciente",size=9)
    nombre = fields.Char(string="Nombre", required=True, index=True,help="nombre del paciente", size=100) 
    apellidos = fields.Char(string="Apellidos", required=True, index=True,help="nombre del paciente", size=100) 
    tlf = fields.Char(string="Telefono", required=True, index=True,help="TLF del paciente", size=20) 
    email = fields.Char(string="Email",required=True,index=True,help="El email del paciente",size=9)
    fecha = fields.Date()
    fotografia = fields.Binary()

    visitas = fields.One2many("medico.visitas_model","paciente",string="visitas")
    nvisitas= fields.Integer(string="visitas",help="numero de visitas",compute="_calcVisitas")
    edad = fields.Integer()
    def eliminarelhistorial(self):
        self.ensure_one()
        for rec in self.visitas:
            rec.unlink()
        return True    
    @api.depends("visitas")
    def _calcVisitas(self):
        self.nvisitas = len(self.visitas)
        for rec in self.visitas:
            rec.detalle
    @api.constrains("dni")
    def validoDNI(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[8]
        letra.upper()
        num = int(self.dni[:8])
        if tabla[num%23]!=letra:
            raise ValidationError("Dni es invalido")
    @api.constrains("email")
    def validoEmail(self):
        if "@" not in self.email:
            raise ValidationError("email es invalido")
    @api.constrains("fecha")
    def _compute_edad(self):
        hoy = date.today()
        fechanacimiento=self.fecha
        edad = hoy.year - fechanacimiento.year - ((hoy.month, hoy.day) < (fechanacimiento.month, fechanacimiento.day))
        if edad <18:
            raise ValidationError("Es menor de edad")
   
