from unittest import TestCase
import requests

class TestRoot(TestCase):
    def setUp(self) -> None:
        self.response_should_contan = {
            "message": "Welcome to To-do Full stack Application."
        }
        
    def test_task_endpoint(self):
        response = requests.get("http://localhost:8000/task/")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIsInstance(json_data, dict, "Task data is not a valid dictionary")
        self.assertIn('task', json_data, 'response data doesnot have proper key-value pair')    
        self.assertIsInstance(json_data.get("task"), list, "Not valid tasks")