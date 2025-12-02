# Tarea15 1ºModulo Odoo
Manuel Carrera Pazó - 2ºDAM

--------

## 1º PASO
Para iniciar debemos levantar el contenedor con:  
```bash
docker compose up
```

A continuación, debemos ejecutar este comando para acceder al contenedor web de Odoo18, en el crearemos la carpeta MaquinaCafe dentro de la carpeta local extra-addons:  
```bash
docker exec -it odoo18_web odoo scaffold MaquinaCafe /mnt/extra-addons
```  
<img width="999" height="26" alt="image" src="https://github.com/user-attachments/assets/cc887fd1-ca26-4295-829a-1cac602901f9" />

----------

## 2º PASO  
Cuando ya tenemos la estructura de las carpetas creada modificamos el archivo `./addons/maquina_cafe/_manyfest_.py`:
<br>   
<img width="1920" height="1005" alt="image" src="https://github.com/user-attachments/assets/b02e5ec0-648f-41e6-ac9a-441b4fb8d7d0" />


```bash
# -*- coding: utf-8 -*-
{
    'name': "Maquina Cafe",
    'summary': "Modulo para calcular café según nivel de sueño",
    'description': """
        Recomienda bebidas según el nivel de sueño:
        • 1 a 3 → Café con leche
        • 4 a 6 → Café solo largo
        • 7 a 9 → Café solo larguísimo
        • 10 → Inyección de adrenalina
    """,
    'author': "Manuel Carrera",
    'website': "https://www.manuelcarrera.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
```
-------

## 3º PASO
Posteriormente tendremos que modificar el archivo `./addons/maquina_cafe/models/models.py` donde añadiremos el código para la funcionalidad de nuestro modulo:  
<br>  
<img width="1920" height="1005" alt="image" src="https://github.com/user-attachments/assets/08352b99-cc9a-4a2b-9e08-444e8fd9b3f1" />

<br>  

```bash
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
```  

-------

## 4º PASO
Por último configuraremos el archivo `./addons/maquina_cafe/views/views.xml`, el cual define las vistas de formulario y lista, la acción para abrirlas y el menú en la interfaz:
<br>  
<img width="1920" height="1005" alt="image" src="https://github.com/user-attachments/assets/44242584-705f-49a8-949e-5f866bbf9f9b" />

<br>  

```bash
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Acción -->
    <record id="action_maquina_cafe" model="ir.actions.act_window">
        <field name="name">Máquina de Café</field>
        <field name="res_model">maquina.cafe</field>
        <field name="view_mode">list,form</field>
    </record>

    <!-- Menú -->
    <menuitem id="menu_maquina_cafe_root" name="Máquina de Café"/>
    <menuitem id="menu_maquina_cafe" name="Registros" parent="menu_maquina_cafe_root" action="action_maquina_cafe"/>

    <!-- Vista lista -->
    <record id="view_maquina_cafe_list" model="ir.ui.view">
        <field name="name">maquina.cafe.list</field>
        <field name="model">maquina.cafe</field>
        <field name="arch" type="xml">
            <list>
                <field name="alumno"/>
                <field name="nivel_sueno" string="Nivel de Sueño"/>
                <field name="bebida_recomendada"/>
            </list>
        </field>
    </record>

    <!-- Vista formulario SIMPLE -->
    <record id="view_maquina_cafe_form" model="ir.ui.view">
        <field name="name">maquina.cafe.form</field>
        <field name="model">maquina.cafe</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="alumno"/>
                        <field name="nivel_sueno" string="Nivel de Sueño"/>  
                        <field name="bebida_recomendada" readonly="1"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```
------

## 5º PASO
También debemos modificar el archivo `./addons/maquina_cafe/security/ir.model.access.csv`, que define los permisos de acceso a los modelos de datos, especificando qué usuarios pueden leer, escribir, crear o eliminar registros en cada tabla de la base de datos del módulo.  
<br>  

<img width="1920" height="1005" alt="image" src="https://github.com/user-attachments/assets/a6d1ff01-9b50-40a3-b4ed-5777dff8410c" />



