#!/usr/bin/env python3

import unittest
import stratify_test_1

class FailureMessageTest(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(False, 'failure message goes here')

if __name__ == '__main__':
    unittest.main()
