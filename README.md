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
<img width="1920" height="1047" alt="image" src="https://github.com/user-attachments/assets/260f130c-f074-4fc0-b566-e9648156267e" />

```bash
# -*- coding: utf-8 -*-
{
    'name': "MaquinaCafe",

    'summary': "Modulo para calcular cuanto café se necesita según la cantidad de sueño",

    'description': """
        ● 1 a 3 → Café con leche
        ● 4 a 6 → Café solo largo
        ● 7 a 9 → Café solo larguísimo
        ● 10 → Inyección de adrenalina
    """,

    'author': "Manuel Carrera",
    'website': "https://www.manuelcarrera.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```
-------

## 3º PASO
Posteriormente tendremos que modificar el archivo `./addons/maquina_cafe/models/models.py` donde añadiremos el código para la funcionalidad de nuestro modulo:  
<br>
```bash
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class BebidaSueño(models.Model):
    _name = 'bebida.sueño'
    _description = 'Recomendación de Bebida por Sueño'
    _rec_name = 'alumno'

    alumno = fields.Char(
        string='Alumno',
        required=True,
        help='Nombre completo del alumno'
    )

    nivel_sueño = fields.Integer(
        string='Nivel de Sueño',
        required=True,
        default=1,
        help='Nivel de sueño del 1 al 10',
        min=1,
        max=10
    )

    bebida_recomendada = fields.Char(
        string='Bebida Recomendada',
        compute='_calcular_bebida',
        store=True,
        help='Bebida recomendada según el nivel de sueño'
    )

    @api.depends('nivel_sueño')
    def _calcular_bebida(self):
        for registro in self:
            sueño = registro.nivel_sueño

            if 1 <= sueño <= 3:
                bebida = 'Café con leche'
            elif 4 <= sueño <= 6:
                bebida = 'Café solo largo'
            elif 7 <= sueño <= 9:
                bebida = 'Café solo larguísimo'
            elif sueño == 10:
                bebida = 'Inyección de adrenalina'
            else:
                bebida = 'ERROR: Nivel no válido'

            registro.bebida_recomendada = bebida
```  
