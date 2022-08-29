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
                                string="unidad")



    #TOMA LA FECHA Y LA HORA DE FORMA AUTOMATICA DEL SERVIDOR
    fecha_hora = fields.Datetime(string="Fecha y Hora",
                                  default=lambda self: fields.Datetime.now(), readonly=True)

    # TOMA EL USUARIO QUE SE LOGUEA
    recibe = fields.Many2one('res.users','Recibe', default=lambda self: self.env.user, readonly=True)

    """
    el campo se entrega a ..... queda pendiente pues aun no se como elaborarlo
    """

    solitudes_ids = fields.One2many(
        comodel_name='solicitudes',
        inverse_name='solicitud_id',
        string='Solitudes')
    numero = fields.Char()

    @api.onchange("direccion")
    def _onchange_dominion_user_id(self):
            return {"domain": {"unidad": [("nombre_area.id","=","depende_superior.id")]}}



class solicitudes(models.Model):
    _name = 'solicitudes'

    serie = fields.Char(string="Serie")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    inventario = fields.Char(string="Inventario")
    descripcion = fields.Text(string="Descripcion")
    ubicacion = fields.Char(string="Ubicacion")
    ext = fields.Char(string="Ext")
    equipo = fields.Many2one(comodel_name="tipo_de_equipo")
    situacion  =fields.Many2one(comodel_name="situacion")
    tipo_solicitud = fields.Selection([('computo', 'Computo'),
                                       ('telefonia', 'Telefonia'),
                                       ('redes', 'Redes'),
                                       ('sistemas', 'Sistemas'),
                                       ('diseño', 'Diseño'),
                                       ('prestamos', 'Prestamos'),
                                       ('administracion', 'Administracion')],
                                      string="Tipo de Solicitud", default="computo")
    solicitud_id = fields.Many2one(comodel_name="datos_generales")
    responsable = fields.Many2one(comodel_name="res.users")
    fecha_evento_inicio = fields.Date(string="Fecha del Evento")
    hora_evento = fields.Char(String="Hora Del evento")
    hora_evento_entrega = fields.Char(String="Hora De Entrega")


    """
    FALTAN LOS CAMPOS EQUIPO NO SE A CREADO EL MODELO AUN, SITUACION FALTA CREAR EL CAMPO,
    RESPONSABLE QUE APUNTE A LOS USUARIOS DEL GRUPO DIC
    """

class prueba(models.Model):
    _inherit ="product.template"





