# coding: utf-8

import unittest

class TupleBasicTest(unittest.TestCase):
    '''タプルの基本的な使い方を確認する
    '''

    def test_creation(self):
        # タプルを生成する
        t1 = ('ギン', 'ギラ', 'ギン')
        self.assertIsInstance(t1, tuple)

        # 実践的な場面で使うことはまずないが空のタプルを生成する
        t2 = ()
        self.assertIsInstance(t2, tuple)

        # 要素数が 1 のタプルについては `,` が必須となるため注意が必要
        t3 = ('さりげなく', )
        self.assertIsInstance(t3, tuple)
        s1 = ('さりげなく')
        self.assertIsInstance(s1, str)

    def test_access(self):
        # タプルの要素にアクセスする
        t1 = ('炎', '天', '下')

        self.assertEqual(t1[0], '炎')
        self.assertEqual(t1[1], '天')

        self.assertEqual(t1[-1], '下')

        self.assertEqual(t1[0:2], ('炎', '天'))

    def test_conversion(self):
        l1 = ('岡山', 15)
        self.assertIsInstance(tuple(l1), tuple)

        t1 = ('香川', 18)
        self.assertEqual(list(t1), ['香川', 18])

    def test_methods(self):
        self.assertEqual((3, 4, 4, 5).count(4), 2)
        self.assertEqual((3, 4, 4, 5).index(5), 3)

    def test_in(self):
        self.assertTrue(3 in (3, 4, 4, 5))
        self.assertFalse(108 in (3, 4, 4, 5))
