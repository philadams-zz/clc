# -*- coding: utf-8 -*-

from .context import clc

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_handles_empty_input(self):
        assert False


if __name__ == '__main__':
    unittest.main()
