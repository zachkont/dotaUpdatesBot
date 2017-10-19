import unittest
import utils

import telebot.types


class TestUtilFunctions(unittest.TestCase):
    """Tests for `utils.py`"""

    def setUp(self):
        self.dummy_user = telebot.types.User(0, 'dummy')
        self.dummy_chat = telebot.types.Chat(0, 'private')
        self.dummy_message = telebot.types.Message(0, self.dummy_user, 0, self.dummy_chat, 'text', {})

    def test_is_getCID_cid(self):
        """Does getCID correctly return a message's chat ID?"""

        dummy_cid = self.dummy_message.chat.id
        get_cid_cid = utils.getCID(self.dummy_message)

        self.assertEquals(dummy_cid, get_cid_cid)


if __name__ == '__main__':
    unittest.main()
