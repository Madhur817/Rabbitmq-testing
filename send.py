#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
msg = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='', routing_key='hello', body=msg)
print(" [x] Sent ", msg)
connection.close()
