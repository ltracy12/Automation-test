# coding=utf-8

'''
Created on Jan25, 2021
@author: Claire
Project: testcase baidu login
'''

import unittest


class BaiDuTest(unittest.TestCase):
    def setUp(self):
        print('Start baidu testcase')

    def test_baidu_case1(self):
        '''This is the first test case.'''
        print('this is baidu case 1')
        youdao = 'baidu'
        self.assertEqual(youdao, 'baidu', msg='the message is not baidu')

    def test_baidu_case2(self):
        print('this is baidu case 2')
        youdao = 'baidu'
        self.assertEqual(youdao, 'baidu', msg='the message is not baidu')

    def tearDown(self):
        print('Finish baidu testcase')


if __name__ == '__main__':
    unittest.main()
