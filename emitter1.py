#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

rk = 'T1'

if len(sys.argv) > 1:
    message = ' '.join(sys.argv[1:])
else:
    sys.stderr.write("Adiciona el mensaje a transmitir. \n")
    sys.exit(1)
channel.basic_publish(exchange='direct_logs', routing_key=rk, body=message)
print(" [x] Enviaste %r a la cola %r" % (message, rk))
connection.close()