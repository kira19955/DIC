from odoo import fields, models, api


class TipoDeMantenimiento (models.Model):
    _name = 'tipo_de_mantenimiento'

    name = fields.Char(string="Descripción")

class mantenimiento(models.Model):
    _name = 'mantenimiento'

    name = fields.Char(string="Descripción")
    tipo = fields.Many2one(comodel_name="tipo_de_mantenimiento")
    costo = fields.Char(string="Costo")

class TipoDeEquipo(models.Model):
    _name = 'tipo_de_equipo'
    _description = 'Catalogo de los diferentes tipos de equipos que hay'

    name = fields.Char(string="Descripción")

class Situacion(models.Model):
    _name = 'situacion'
    _description = 'Catalogo de los diferentes tipos de situacion'

    name = fields.Char(string="Descripción")

class CentroDeServicios(models.Model):
    _name = 'centro_de_servicios'
    _description = 'Catalogo de centro de servicios'

    name = fields.Char(string="Descripción")
    tel = fields.Char(string="Teléfono")
    direccion = fields.Char(string="Dirección")


"""
FALTAN LOS MODELOS DE CATALOGO DE MATERIAL Y 
CATALOGO DE UNIDAD DE MEDIDA, PARA CUESTIONES DE INVENTARIO 
CHECAR EL MODULO DE INVENTARIO DE ODOO Y VER COMO FUNCIONA
"""