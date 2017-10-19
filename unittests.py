import unittest
import utils
import time

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

    def setUp(self):
        self.dummy_user = telebot.types.User(0, 'dummy')
        self.dummy_chat = telebot.types.Chat(0, 'private')
        self.dummy_message = telebot.types.Message(0, self.dummy_user, 0, self.dummy_chat, 'text', {})

    def test_is_getCID_cid(self):
        """Does getCID correctly return a message's chat ID?"""

        dummy_cid = self.dummy_message.chat.id
        get_cid_cid = utils.getCID(self.dummy_message)

        self.assertEquals(dummy_cid, get_cid_cid)

    def test_is_5_seconds_in_time(self):
        """Is a 5-second delay successfully determined to be in time?"""

        time_five_seconds_earlier = int(time.time()) - 5
        message_five_seconds_earlier = self.dummy_message_at_time(time_five_seconds_earlier)

        self.assertTrue(utils.intime(message_five_seconds_earlier))

    def test_is_10_seconds_in_time(self):
        """Is a 10-second delay successfully determined not to be in time?"""

        time_ten_seconds_earlier= int(time.time()) - 10
        message_ten_seconds_earlier = self.dummy_message_at_time(time_ten_seconds_earlier)

        self.assertFalse(utils.intime(message_ten_seconds_earlier))


if __name__ == '__main__':
    unittest.main()
