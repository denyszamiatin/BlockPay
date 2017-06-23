import unittest
import unittest.mock
import models


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = models.User('Bill', 'XXXX', 'a@a.org')

    def test_email(self):
        self.assertEqual(self.user.email, 'a@a.org')

    def test_first_name(self):
        self.assertEqual(self.user.first_name, 'Bill')

    def tearDown(self):
        pass


class TestKeyGenerator(unittest.TestCase):

    @unittest.mock.patch('models.r')
    def test_add(self, m):
        m.return_value = 2
        self.assertEqual(models.add(2, 3), 7)
        m.return_value = 3
        self.assertEqual(models.add(2, 3), 9)