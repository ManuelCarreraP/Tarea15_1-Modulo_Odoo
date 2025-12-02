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

