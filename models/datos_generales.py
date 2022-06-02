from odoo import fields, models, api



class datosgenerales(models.Model):
    _name = 'datos_generales'

    name = fields.Char(string = "Solicitante")
    tipo_peticion = fields.Selection(selection=[('memo', 'Memo'),
                                                ('oficio', 'Oficio'),
                                                ('telefonico', 'Telefonico'),
                                                ('personal', 'Personal')],
                                     string="Tipo de Petición")

    direccion = fields.Many2one(comodel_name="directorio_municipal.directorio_municipal",
                                string="Direccion")
    unidad = fields.Many2one(comodel_name="directorio_municipal.directorio_municipal",
                                string="Direccion")



    #TOMA LA FECHA Y LA HORA DE FORMA AUTOMATICA DEL SERVIDOR
    fecha_hora = fields.Datetime(string="Fecha y Hora",
                                  default=lambda self: fields.Datetime.now(), readonly=True)

    # TOMA EL USUARIO QUE SE LOGUEA
    recibe = fields.Many2one('res.users','Recibe', default=lambda self: self.env.user, readonly=True)

    """
    el campo se entra a ..... queda pendiente pues aun no se como elaborarlo
    """

class solicitudes(model.Model):
    _name = 'solicitudes'

    serie = fields.Char(string="Serie")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    inventario = fields.Char(string="Inventario")
    descripcion = fields.Text(string="Inventario")
    ubicacion = fields.Char(string="Ubicacion")
    ext = fields.Char(string="Ext")
    """
    FALTAN LOS CAMPOS EQUIPO NO SE A CREADO EL MODELO AUN, SITUACION FALTA CREAR EL CAMPO,
    RESPONSABLE QUE APUNTE A LSO USUARIOS DEL GRUPO DIC
    """





