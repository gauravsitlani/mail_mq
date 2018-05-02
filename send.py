import pika

'''
creating the connection , by default we have specified the name of host as local host for a local machine else we can specify the ip address in the place.
'''

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

'''
creating a hello queue
'''

channel.queue_declare(queue='hello')

'''
the queue name needs to be specified in the routing parameter

'''

channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
print(" [x] Sent 'Hello World!'")


'''
closing the connection to flush the buffer 
'''

connection.close()


