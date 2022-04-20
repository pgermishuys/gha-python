from unittest import TestCase

class TryTesting(TestCase):
    def test_hello_world(self):
        assert 1 == 1
    def test_failing(self):
        assert 1 == 2