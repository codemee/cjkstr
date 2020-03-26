import unittest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import cjkstr

class TestCJKStr(unittest.TestCase):
    def test_count_cjk_chars(self):
        self.assertEqual(cjkstr.count_cjk_chars("hello"), 0)
        self.assertEqual(cjkstr.count_cjk_chars("測試一下"), 4)
        self.assertEqual(cjkstr.count_cjk_chars("測試 English"), 2)
        self.assertEqual(cjkstr.count_cjk_chars("試してみる"), 5)
        self.assertEqual(cjkstr.count_cjk_chars("Python 的日文叫パイソン"), 8)
        self.assertEqual(cjkstr.count_cjk_chars("파파이썬 테스트"), 7)
        self.assertEqual(cjkstr.count_cjk_chars("Python 的韓文叫파이썬"), 7)
        with self.assertRaises(TypeError):
            cjkstr.count_cjk_chars(1)
        with self.assertRaises(TypeError):
            cjkstr.count_cjk_chars(23.4)
        with self.assertRaises(TypeError):
            cjkstr.count_cjk_chars(True)
        with self.assertRaises(TypeError):
            cjkstr.count_cjk_chars(5+3j)

