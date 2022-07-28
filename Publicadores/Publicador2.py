#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

if len(sys.argv) > 1:
    severity = sys.argv[1] 
else:
    sys.stderr.write("Adiciona la cola a transmitir: [T1] [T2]\n")
    sys.exit(1)
if len(sys.argv) > 2:
    message = ' '.join(sys.argv[2:])
else:
    sys.stderr.write("Adiciona el mensaje a transmitir. \n")
    sys.exit(1)
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Enviaste %r a la cola %r" % (message, severity))
connection.close()
