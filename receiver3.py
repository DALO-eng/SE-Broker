#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# connection = pika.BlockingConnection(pika.ConnectionParameters('10.14.16.190',5672,'/',pika.PlainCredentials('user', 'pass')))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result1 = channel.queue_declare(queue='Q1', exclusive=False)
result2 = channel.queue_declare(queue='Q2', exclusive=False)

channel.queue_bind(exchange='direct_logs', queue='Q1', routing_key='T1')
channel.queue_bind(exchange='direct_logs', queue='Q2', routing_key='T2')

print(' [*] Esperando por mensajes. Pulsar CTRL+C para cerrar.')

def callback(ch, method, properties, body):
    print(" [x] Recibiste %r por %r" % (body.decode(), method.routing_key))

channel.basic_consume(queue='Q1', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='Q2', on_message_callback=callback, auto_ack=True)

channel.start_consuming()