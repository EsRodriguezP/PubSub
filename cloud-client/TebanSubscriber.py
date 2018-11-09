import time
import ast

from google.cloud import pubsub_v1

project_id = "project_id"
subscription_name = "subscription_name"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    # print type(message.message_id)
    # print message.message_id
    # if str(message.message_id) == '281416710530946':
    #     print message


#------------------works------
    # print message
    if message.attributes:
        # print message
        data_dict = dict(message.attributes)
        if message.attributes['id_user'] == '865':
            print message
    #         time.sleep(100)
    message.ack()
    # elif message.data:
    #     print message
    #     if message.data[message.data.find('id_user')+8:message.data.find(', g')] == '864':
    #         print message

print('Listening for messages on {}'.format(subscription_path))
while True:
    subscriber.subscribe(subscription_path, callback=callback)
    time.sleep(10)

    # The subscriber is non-blocking. We must keep the main thread from
    # exiting to allow it to process messages asynchronously in the background.
    # while True:
    #     time.sleep(70)