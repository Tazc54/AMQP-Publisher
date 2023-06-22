#!/usr/bin/env python
import pika
import sys
from utils import get_url


params = pika.URLParameters(get_url())
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = input("Ingrese el log a enviar: ")

try:
    while message != 'exit':
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(" [x] Sent %r" % message)
        message = input("Ingrese el log a enviar: ")
except KeyboardInterrupt:
    connection.close()