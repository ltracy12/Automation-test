# coding=utf-8

'''
Created on Jan25, 2021
@author: Claire
Project: testcase youdao login
'''

import unittest

class YouDaoTest(unittest.TestCase):
    def setUp(self):
        print('Start youdao testcase')

    def test_youdao_case1(self):
        print('this is youdao case 1')
        youdao = 'youdao'
        self.assertEqual(youdao, 'youdao', msg='the message is not youdao')

    def tearDown(self):
        print('Finish youdao testcase')


if __name__ == '__main__':
    unittest.main()
