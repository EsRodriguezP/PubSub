import time
import datetime

from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())


while True:
    data = raw_input()
    data = data.encode('utf-8')
    attributes = {'cx': "-74.0941958",
                  'cy': "4.6038614",
                  'date': "2018-11-07 16:53:53", 
                  'id_user': "525"}
    message_future = publisher.publish(topic_path, data=data, **attributes)
    message_future.add_done_callback(callback)
    print('Published message IDs:')

    # We must keep the main thread from exiting to allow it to process
    # messages in the background.
    # while True:
    time.sleep(5)
