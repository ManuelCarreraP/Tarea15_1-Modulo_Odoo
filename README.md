# Tarea15 1ºModulo Odoo
Manuel Carrera Pazó

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



```  
