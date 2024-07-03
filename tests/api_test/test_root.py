from unittest import TestCase
import requests

class TestRoot(TestCase):
    def setUp(self) -> None:
        self.response_should_contan = {
            "message": "Welcome to To-do Full stack Application."
        }
        return super().setUp() 
    def test_root_endpoint(self):
        response = requests.get("http://localhost:8000")
        self.assertEqual(response.status_code, 200)