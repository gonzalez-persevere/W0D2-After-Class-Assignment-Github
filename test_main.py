# test_main.py
import unittest
from main import hello_world
from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from Arnulfo Gonzalez!")
    
    def test_greet_person(self):
        self.assertEqual(greet_person("Arnulfo"), "Hello, Arnulfo!")

if __name__ == '__main__':
    unittest.main()