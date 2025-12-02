# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MaquinaCafe(models.Model):
    _name = 'maquina.cafe'
    _description = 'Máquina de Café - Recomendación por Sueño'
    _rec_name = 'alumno'

    alumno = fields.Char(
        string='Alumno',
        required=True,
        help='Nombre del alumno'
    )

    nivel_sueno = fields.Integer(
        string='Nivel de Sueño',
        required=True,
        default=1,
        help='Nivel de sueño (1-10)',
        min=1,
        max=10
    )

    bebida_recomendada = fields.Char(
        string='Bebida Recomendada',
        compute='_compute_bebida_recomendada',
        store=True,
        readonly=True
    )

    @api.depends('nivel_sueno')
    def _compute_bebida_recomendada(self):
        for record in self:
            nivel = record.nivel_sueno

            if 1 <= nivel <= 3:
                bebida = 'Café con leche'
            elif 4 <= nivel <= 6:
                bebida = 'Café solo largo'
            elif 7 <= nivel <= 9:
                bebida = 'Café solo larguísimo'
            elif nivel == 10:
                bebida = 'Inyección de adrenalina'
            else:
                bebida = 'Nivel no válido'

            record.bebida_recomendada = bebida

    @api.constrains('nivel_sueno')
    def _check_nivel_sueno(self):
        for record in self:
            if record.nivel_sueno < 1 or record.nivel_sueno > 10:
                raise models.ValidationError('El nivel de sueño debe estar entre 1 y 10')