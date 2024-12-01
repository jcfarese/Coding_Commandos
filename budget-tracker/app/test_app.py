import unittest
from app import app

class TestSpendingTracker(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expense Tracker', response.data)

    def test_add_transaction_page(self):
        response = self.app.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Expense', response.data) 


if __name__ == '__main__':
    unittest.main()
