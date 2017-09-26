# IV-Proyecto

## Repositorio para el proyecto que se realizará para la asignatura Infraestructura Virtual

## Bot de telegram para buscar viajes en blablacar

El proyecto consistiría en un bot de telegram, que nos proporcionaría información acerca de viajes disponibles en blablacar haciendo uso de su API mediante un servicio web. Algunas de las funcionalidades de este bot podrían ser:
- Buscar próximos viajes introduciendo origen y destino.
- Ordenar estos viajes por precio, o por hora de salida.
- Buscar todos los viajes disponibles introduciendo solo el origen.
- Marcar viajes como favoritos, para tener la posibilidad de recordarlos o verlos más tarde.

### Herramientas que se usarán para desarrollar el proyecto:

- Como lenguaje de programación se usará python 3.
- Se usará la [API de Blablacar](https://dev.blablacar.com/docs/versions/1.0) para acceder a los datos de viajes publicados.
- Se usará [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) para desarrollar el bot de Telegram.
- Se usará un servidor de base de datos para almacenar los viajes marcados como favoritos de cada usuario.
