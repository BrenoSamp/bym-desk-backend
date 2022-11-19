import pika, json

params = pika.URLParameters('amqps://czqxwpup:tBLB3TcxbjxUp7-sbk63mrzLqROKS4Xf@albatross.rmq.cloudamqp.com/czqxwpup')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='create_ticket', body=json.dumps(body), properties=properties)