#!/usr/bin/env python
import json
import errno

class SubscriberManager:
    def __init__(self, filename):
        self.filename = filename

    def subscribers(self):
        try:
            with open(self.filename, 'r') as subscriber_file:
               subscribers = json.load(subscriber_file)
               return subscribers
        except IOError as e:
            if e.errno is errno.ENOENT:
                return {}
            else:
                raise

    def add(self, subscriber_id, subscriber_name):
        current_subscribers = self.subscribers()
        if subscriber_id in current_subscribers and subscriber_name == current_subscribers[subscriber_id]:
            return False
        subscriber = {subscriber_id: subscriber_name}
        current_subscribers.update(subscriber)

        with open(self.filename, 'w') as subscriber_file:
            json.dump(current_subscribers, subscriber_file)
            return True
        return False

    def delete(self, subscriber_id):
        current_subscribers = self.subscribers()
        subscriber_id = str(subscriber_id)
        if str(subscriber_id) not in current_subscribers.keys():
            return False
        del current_subscribers[subscriber_id]
        with open(self.filename, 'w') as subscriber_file:
            json.dump(current_subscribers, subscriber_file)
            return True
        return False
