#!/usr/bin/env python
import pika
import sys

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.17',5672,'/',pika.PlainCredentials('user', 'pass')))

q = 'Q1'
RK = 'T1'

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result2 = channel.queue_declare(queue=q, exclusive=False)

channel.queue_bind(exchange='direct_logs', queue=q, routing_key=RK)

print(' [*] Esperando por mensajes. Pulsar CTRL+C para cerrar.')

def callback(ch, method, properties, body):
    print(" [x] Recibiste %r por %r" % (body.decode(), method.routing_key))

channel.basic_consume(queue=q, on_message_callback=callback, auto_ack=True)

channel.start_consuming()