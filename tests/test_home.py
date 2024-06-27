import pytest
from unittest import TestCase

from selenium.webdriver import Firefox

import time

class TestHome(TestCase):
    def setUp(self) -> None:
        self.firefox = Firefox()
        
    def test_home_page(self):
        res = self.firefox.get("http://localhost:4200/")
        time.sleep(2)
        
    
    def tearDown(self) -> None:
        self.firefox.quit()