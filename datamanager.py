#!/usr/bin/env python
import json
import errno

class DictManager:
    """Manages the writing of key,value pairs to disk and reading back from disk"""

    def __init__(self, filename):
        self.filename = filename

    def data(self):
        """Return all the data stored in this manager"""
        try:
            with open(self.filename, 'r') as data_file:
               data = json.load(data_file)
               return data
        except IOError as e:
            if e.errno is errno.ENOENT:
                return {}
            else:
                raise

    def add(self, data):
        """Add (key, value) item to file object"""
        current_data = self.data()
        key, value = data
        if key in current_data and value == current_data[data]:
            return False
        item = {key: value}
        current_data.update(item)

        with open(self.filename, 'w') as subscriber_file:
            json.dump(current_data, subscriber_file)
            return True
        return False

    def delete(self, key):
        """Delete a data item based on the given key"""
        current_data = self.data()
        key = str(key)
        if key not in current_data.keys():
            return False
        del current_data[key]
        with open(self.filename, 'w') as subscriber_file:
            json.dump(current_data, subscriber_file)
            return True
        return False
