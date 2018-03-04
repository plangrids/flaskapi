from flaskapi import app
import unittest
import requests
import json

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5001"
        self.app = app.test_client()

    def test_app_1(self):
        response = requests.get(self.url,headers={'Accept': 'application/json'})
        self.assertEqual(response.json(), GOOD_JSON_RESPONSES)

    def test_app_2(self):
        response = requests.get(self.url)
        self.assertEqual(response.text, GOOD_TEXT_RESPONSES)

GOOD_JSON_RESPONSES = {"message": "Good Morning"}
GOOD_TEXT_RESPONSES = '<p> Hello, World </p>'

if __name__ == "__main__":
    unittest.main()

