#!/usr/bin/env python
from asyncio import queues
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='https://yromariogh.pagekite.me'))
channel = connection.channel()


channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Digita la(s) cola(s) a recibir: [T1] [T2]\n")
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Esperando por mensajes. Pulsar CTRL+C para cerrar.')


def callback(ch, method, properties, body):
    print(" [x] Recibiste %r por %r" % (body.decode(), method.routing_key))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()