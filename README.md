# Bot de telegram para buscar viajes en blablacar
[![Build Status](https://travis-ci.org/ajpelaez/IV-Proyecto.svg?branch=master)](https://travis-ci.org/ajpelaez/IV-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

El proyecto consistiría en un bot de telegram, que nos proporcionaría información acerca de viajes disponibles en blablacar haciendo uso de su API mediante un servicio web. Algunas de las funcionalidades de este bot podrían ser:
- Buscar próximos viajes introduciendo origen y destino.
- Ordenar estos viajes por precio, o por hora de salida.
- Buscar todos los viajes disponibles introduciendo solo el origen.
- Marcar viajes como favoritos, para tener la posibilidad de recordarlos o verlos más tarde.

### Herramientas que se usarán para desarrollar el proyecto:

- Como lenguaje de programación se usará python 3.
- Se usará la [BlaBlaCar API Client Python Library](https://github.com/arrrlo/BlaBlaCar-Client-Api) para acceder a los datos de viajes publicados.
- Se usará [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) para desarrollar el bot de Telegram.
- Se usará [Pocha](https://github.com/rlgomes/pocha) como herramienta de apoyo para la realización de los tests.
- Se usará un servidor de base de datos para almacenar los viajes marcados como favoritos de cada usuario.
- Para el despliegue en la nube se usará la plataforma de [AWS](https://aws.amazon.com/es/).

### Requisitos y dependencias:

~~~
pip3 install git+git://github.com/ajpelaez/BlaBlaCar-Client-Api@master
pip3 install pyTelegramBotAPI
pip3 install git+git://github.com/ajpelaez/pocha
~~~
