import unittest
import os
import sqlite3
from app import app, init_db

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        self.test_db = 'test_database.db'
        self.app = app.test_client()
        self.app.testing = True
        import app as app_module
        app_module.DATABASE = self.test_db
        app_module.init_db()

    def tearDown(self):
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except:
                pass

    def test_get_index_empty(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'class="todo-list"', response.data)

    def test_post_add_todo(self):
        response = self.app.post('/add', data={'title': '공부하기'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('공부하기', response.data.decode('utf-8'))

    def test_get_index_after_add(self):
        self.app.post('/add', data={'title': '공부하기'}, follow_redirects=True)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('공부하기', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
