# Creación de Broker

## Requerimientos

* **Instalar rabbitMQ**
Para instalar rabbitMQ puede seguir el tutorial del siguiente link: [Instalación rabbitMQ en Ubuntu](https://computingforgeeks.com/how-to-install-latest-rabbitmq-server-on-ubuntu-linux/)

* **Instalar nodeJS y NPM**
Para instalar node y npm puede seguir el tutorial del siguiente link: [Instalación NodeJS en Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04)

### Javascript

Una vez baje el repositorio deberá ejecutar el comando:

```
npm install
```
#### Receivers

Para que los receivers de JS muestren los mensajes de su respectiva cola, deberá ejecutar el siguiente comando:
```
node receiver1.js
```
(Esto para el receiver correspondiente)

#### Emitters

Para que los emitters de JS envien los mensajes de su respectiva cola, deberá ejecutar el siguiente comando:
```
node emitter1.js Mi mensaje
```
(Esto para el emitter correspondiente)

### Python

Se debe instalar el lenguaje [Python](https://www.python.org/downloads/)
Se debe instalar el sistema de gestión de paquetes [pip](https://pypi.org/project/pip/)
Finalmente se instala la librería [pika](https://pypi.org/project/pika/)

#### Receivers

Para que los receivers de Python muestren los mensajes de su respectiva cola, deberá ejecutar el siguiente comando:
```
python receiver1.py
```
(Esto para el receiver correspondiente)

#### Emitters

Para que los emitters de Python envien los mensajes de su respectiva cola, deberá ejecutar el siguiente comando:
```
python emitter1.py Mi mensaje
```
(Esto para el emitter correspondiente)