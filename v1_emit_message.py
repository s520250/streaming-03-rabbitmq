"""
    This program sends a message to a queue on the RabbitMQ server.

    Sammie Bever - Streaming Data - Module 03 Assignment - January 22, 2023

    Author: Denise Case
    Date: January 14, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# define message variable (as to not repeat yourself throughout the rest of this code)
message = "Message 4 - Module 3 Assignment."
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user - see that I printed a variable using {}
print(" [x] Sent '{}'".format(message))
# close the connection to the server
conn.close()

# ran this file 4 times - changing the 'message' variable each time in order to send 4 messages