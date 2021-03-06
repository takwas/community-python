import unittest

import bcrypt

from app import app
from models import User


class FlaskTestCase(unittest.TestCase):
    user: User

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/auth/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # def test_register_test_user(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/auth/register/test', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_jwt_authentication(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/auth/authenticate-jwt?email=theobouwman98@gmail.com&password=test', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
