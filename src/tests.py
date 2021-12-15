import unittest
import app as tested_app


class SimpleAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_while_input(self):
        self.app.fibonacci_while_loop()
        self.assertEqual()