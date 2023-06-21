# AMQP-Publisher
# This project consist on a work queue and a Publish/subscription Schema.
# new_task.py and worker.py are part of the work queue process.
# emit_log.py and receive_logs.py are part of the publish/subscription process.


# To start this you have to make sure that:
* You have pika installed on your system
* pip install pika
* Docker is running on your system: Then execute the following code on your terminal
* docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management



# to start the work queue
* Run the worker.py  (you can run multiple instances of this script, the queue will then distribute the task into the different workers)
* Run the new_task.py to send a task e.g (python new_task.py First message.)

# to Start the publish/subscription process
* Run the receive_logs.py (This script will receive the logs you send)
* Run the emit_log.py With this script you can send logs e.g. (python emit_log.py This is a log)


