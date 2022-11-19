import pika

params = pika.URLParameters('amqps://czqxwpup:tBLB3TcxbjxUp7-sbk63mrzLqROKS4Xf@albatross.rmq.cloudamqp.com/czqxwpup')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='create_ticket')

def callback(ch, method, properties, body):
    print('Received')
    print(body)

channel.basic_consume(queue='create_ticket', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()