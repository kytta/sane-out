from unittest import TestCase

from sane_out import __version__


class TestSaneOut(TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.0.1")
