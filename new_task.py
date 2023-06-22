#!/usr/bin/env python
import pika
import sys
from utils import get_url


params = pika.URLParameters(get_url())
connection = pika.BlockingConnection(params)
channel = connection.channel()
cola = 'task_queue'
channel.queue_declare(queue=cola, durable=True)

message = input("Ingrese el mensaje: ")
try:
    while message != 'exit':
        channel.basic_publish(
            exchange='',
            routing_key=cola,
            body=message,
            properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
        message = input("Ingrese el mensaje: ")
except KeyboardInterrupt:
    connection.close()