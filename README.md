# Bot de telegram para buscar viajes en blablacar
[![Build Status](https://travis-ci.org/ajpelaez/IV-Proyecto.svg?branch=master)](https://travis-ci.org/ajpelaez/IV-Proyecto)
[![codecov.io Code Coverage](https://img.shields.io/codecov/c/github/ajpelaez/IV-proyecto.svg)](https://codecov.io/gh/ajpelaez/IV-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ajpelaez/IV-Proyecto)

El proyecto consistiría en un bot de telegram, que nos proporcionaría información acerca de viajes disponibles en blablacar haciendo uso de su API mediante un servicio web. Algunas de las funcionalidades de este bot podrían ser:
- Buscar próximos viajes introduciendo origen y destino.
- Ordenar estos viajes por precio, o por hora de salida.
- Buscar todos los viajes disponibles introduciendo solo el origen.
- Marcar viajes como favoritos, para tener la posibilidad de recordarlos o verlos más tarde.

### Herramientas que se usarán para desarrollar el proyecto:

- Como lenguaje de programación se usará python 3.
- Se usará la [BlaBlaCar API Client Python Library](https://github.com/arrrlo/BlaBlaCar-Client-Api) para acceder a los datos de viajes publicados.
- Se usará [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) para desarrollar el bot de Telegram.
- Se usará un servidor de base de datos para almacenar los viajes marcados como favoritos de cada usuario.
- Para desplegar en la nube se usará la plataforma de [AWS](https://aws.amazon.com/es/).

### Requisitos y dependencias:

~~~
pip3 install git+git://github.com/ajpelaez/BlaBlaCar-Client-Api@master
pip3 install pyTelegramBotAPI
pip3 install gunicorn
pip3 install hug
pip3 install coverage
pip3 install codecov
~~~

### TDD e integración continua

Como plataforma para la integración continua este proyecto usa [Travis-CI](https://travis-ci.org/).

![Travis-CI](https://i2.wp.com/blog.fossasia.org/wp-content/uploads/2016/08/travis.png?resize=128%2C128)

Para el desarrollo de este proyecto se usarán las técnicas de desarrollo guiado por pruebas e integración continua. Gracias a las combinaciones de ambas técnicas conseguimos que el proyecto tenga un fácil mantenimiento además de asegurarnos de que en todo momento nuestro software debería funcionar correctamente y sin fallos haciendo exactamente lo que se le pide.

Puede que el desarrollo basado en tests sea un desarrollo más lento y costoso, pero todo ese tiempo que se invierte al principio en la programación de los test, es tiempo que luego ahorraremos al programar nuestras funciones ya que ya sabemos exactamente lo que tenemos que programar, además de que también ahorraremos tiempo en tareas de mantenimiento y resolución de bugs.

### Desplegar en un PaaS

Despliegue http://blablacarapi.herokuapp.com/


![Heroku](https://flowdocs.built.io/assets/blt881a8d2361afdcca/Heroku-128.png)

Como plataforma hemos escogido Heroku ya que además de tener una extensa documentación que nos ha ayudado al desplegar nuestra app, ofrece planes gratuitoss sin límite de tiempo para alojar nuestra aplicación.
Heroku también nos ofrece una gran cantidad de add-ons para nuestra aplicación y nos da la posibilidad de hacer deploys automáticos integrados con nuestro motor de integración continua.

Para poder desplegar nuestra app en Heroku hemos configurado los siguientes ficheros en nuestro repo:

- **Procfile** (Que contiene los workers que ejecutará heroku)
- **app.json** (Que contiene la configuración para que cualquiera pueda hacer deploy de nuestra app fácilmente haciendo click en el icono de Deploy to Heroku)
- **requirements.txt** (Que contiene todas las dependencias de nuestra app)

Para hacer el deploy de nuestra app es tan fácil como seguir los siguientes pasos:
- Hacer click en el boton Deploy to Heroku
- Elegir un nombre y región para la app
- Activar el worker web en la configuración de nuestra app -> resources
![Worker Heroku](https://raw.githubusercontent.com/ajpelaez/IV-Ejercicios/master/imgs/worker-heroku.png)

Para el **deploy automático** cuando hacemos push a GitHub tenemos que configurar las siguientes opciones en la configuración de nuestra app -> deploy
- Seleccionar GitHub como deploy method
![Heroku config](https://raw.githubusercontent.com/ajpelaez/IV-Ejercicios/master/imgs/config-deploy-heroku1.png)

- Activar automatic deploy y marcar la casilla wait for CI to pass before deploy
![Heroku config](https://raw.githubusercontent.com/ajpelaez/IV-Ejercicios/master/imgs/config-deploy-heroku2.png)
