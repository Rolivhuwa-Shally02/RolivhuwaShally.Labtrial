#!/usr/bin/env python3

import unittest

import stratify_test_1

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()
