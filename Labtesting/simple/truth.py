#!/usr/bin/env python3

import unittest
import stratify_test_1

class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
