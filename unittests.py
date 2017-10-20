import unittest
import utils
import time
import os
import json
import telebot.types


class TestUtilFunctions(unittest.TestCase):
    """Tests for `utils.py`"""

    def dummy_message_at_time(self, message_time):
        """Creates new message with attributes from dummy_message at given time"""

        message = telebot.types.Message(self.dummy_message.message_id,
                                        self.dummy_message.from_user,
                                        message_time,
                                        self.dummy_message.chat,
                                        self.dummy_message.content_type,
                                        {})

        return message

    def dummy_message_with_text(self, text):
        """Creates new message with attributes from dummy message with given text as message text"""

        message = telebot.types.Message(self.dummy_message.message_id,
                                        self.dummy_message.from_user,
                                        self.dummy_message.date,
                                        self.dummy_message.chat,
                                        self.dummy_message.content_type,
                                        {'text': text})

        return message

    def setUp(self):
        self.dummy_user = telebot.types.User(0, 'dummy_first_name')
        self.dummy_chat = telebot.types.Chat(0, 'private')
        self.dummy_message = telebot.types.Message(0, self.dummy_user, 0, self.dummy_chat, 'text', {})

    def test_is_getCID_cid(self):
        """Does getCID correctly return a message's chat ID?"""

        dummy_cid = self.dummy_message.chat.id
        get_cid_cid = utils.getCID(self.dummy_message)

        self.assertEquals(dummy_cid, get_cid_cid)

    def test_is_getContent_message_content(self):
        """Does getContent correctly return the contents of a message?"""

        message_content = 'dummy_content'
        message_command = '/dummy_command '
        message_text = message_command + message_content
        message = self.dummy_message_with_text(message_text)

        get_content_content = utils.getContent(message)

        self.assertEquals(message_content, get_content_content)

    def test_is_getContent_of_empty_content_none(self):
        """Does getContent correctly return None when given a message with no content?"""

        message_content = ''
        message_command = '/dummy_command'
        message_text = message_command + message_content
        message = self.dummy_message_with_text(message_text)

        get_content_content = utils.getContent(message)

        self.assertIsNone(get_content_content)

    def test_is_5_seconds_in_time(self):
        """Is a 5-second delay successfully determined to be in time?"""

        time_five_seconds_earlier = int(time.time()) - 5
        message_five_seconds_earlier = self.dummy_message_at_time(time_five_seconds_earlier)

        self.assertTrue(utils.intime(message_five_seconds_earlier))

    def test_is_10_seconds_in_time(self):
        """Is a 10-second delay successfully determined not to be in time?"""

        time_ten_seconds_earlier = int(time.time()) - 10
        message_ten_seconds_earlier = self.dummy_message_at_time(time_ten_seconds_earlier)

        self.assertFalse(utils.intime(message_ten_seconds_earlier))


class TestUtilJSONFunctions(unittest.TestCase):
    """Tests for `utils.py` JSON functions"""

    def setUp(self):
        self.file_path = 'json_function_test'

        # Makes empty file
        open(self.file_path + '.json', 'a').close()

    def test_addUser_adds_user(self):
        """Does addUser correctly add user object to given file?"""

        user_id = 0
        user_name = u'dummy_name'
        empty_json = json.loads('{}')

        user_dict_json = {u'0': u'dummy_name'}  # JSON loads dict elements as unicode strings

        # addUser requires existing JSON
        with open(self.file_path + '.json', 'w') as f:
            json.dump(empty_json, f)

        utils.addUser(user_id, user_name, self.file_path)

        with open(self.file_path + '.json') as f:
            added_user_json = json.loads(f.read())

        self.assertEqual(user_dict_json, added_user_json)

    def test_loadjson_loads_json(self):
        """Does loadjson correctly load json from the given file?"""

        key = u'dummy_key'
        value = u'dummy_value'
        json_dict = {key: value}

        with open(self.file_path + '.json', 'w') as f:
            json.dump(json_dict, f)

        loaded_json = utils.loadjson(self.file_path)

        self.assertEqual(json_dict, loaded_json)

    def test_deljson_deletes_json_keys(self):
        """Does deljson correctly delete JSON entries with given keys?"""

        json_dict = {u'one': u'a', u'two': u'b', u'three': u'c'}
        json_dict_two_deleted = {u'one': u'a', u'three': u'c'}

        with open(self.file_path + '.json', 'w') as f:
            json.dump(json_dict, f)

        utils.deljson(u'two', self.file_path)

        with open(self.file_path + '.json') as f:
            json_dict_after_deljson = json.load(f)

        self.assertEqual(json_dict_two_deleted, json_dict_after_deljson)

    def test_deljson_deletes_json_values(self):
        """Does deljson correctly delete JSON entries with given values?"""

        json_dict = {u'one': u'a', u'two': u'b', u'three': u'c'}
        json_dict_b_deleted = {u'one': u'a', u'three': u'c'}

        with open(self.file_path + '.json', 'w') as f:
            json.dump(json_dict, f)

        utils.deljson(u'b', self.file_path)

        with open(self.file_path + '.json') as f:
            json_dict_after_deljson = json.load(f)

        self.assertEqual(json_dict_b_deleted, json_dict_after_deljson)

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except OSError:
            # File doesn't exist to delete
            pass


if __name__ == '__main__':
    unittest.main()
