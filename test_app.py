import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # sends GET request to the root URL
        result = self.app.get('/')
        # assert the response is correct
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Hello, World!')

if __name__ == "__main__":
    unittest.main()
