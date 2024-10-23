# Dolar MEP APP: API para compra y venta de Dolar Mep con FastAPI 

Esta aplicacion con **FastAPI** simula la compra **compra** y **venta** de bonos.

## Requisitos Previos para instalacion
- **Docker**: Se debe tener instalado Docker para ejecutar el contenedor con solo un par de comandos

## Explicacion
- Se selecciono el uso de FastAPI para la app debido a su facilidad en la construccion de API sencillas, asi como tambien el hecho de generar de manera automática una documentación interactiva basada en OpenAPI (Swagger)
- Se hizo uso del patron Repositorio  para separar la lógica de negocio del acceso a los datos, facilitando el mantenimiento, las pruebas y la escalabilidad del proyecto.

## Cómo Levantar el Proyecto

Para levantar el proyecto, seguir los siguientes pasos:
- Clonar este repositorio
- Agregar a la raiz del proyecto el archivo .env enviado a traves de correo que contiene las credenciales de reMarket
- Abrir la terminal y ubicarse a la altura de main.py
- Ejecutar los siguientes comandos de docker

```bash
docker build -t dolar_mep_app .
docker run -d -p 8000:8000 --name dolar_mep_app dolar_mep_app
```
- Acceder a la url http://localhost:8000/docs
