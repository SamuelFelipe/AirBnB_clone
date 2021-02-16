#!/usr/bin/python3
'''Test to the BaseModel class'''

from models.user import User
import datetime
import unittest


class TestUser(unittest.TestCase):
    '''Test cases to the BaseModel class'''

    def test_id(self):
        '''Test the correct id assignment'''
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)

    def test_datastored(self):
        '''Test the data type stored in the object'''
        test2 = User()
        self.assertEqual(type(test2.id), str)
        self.assertEqual(type(test2.created_at), datetime.datetime)
        self.assertEqual(type(test2.updated_at), datetime.datetime)

    def test_to_dic(self):
        '''Test the correct output of the 'to_dic' method'''
        test3 = User()
        dic = test3.to_dict()
        self.assertEqual(len(dic), 4)
        test3.name = 'Alexander'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 5)
        test3.last_name = 'Milne'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 6)
        for i in dic.values():
            self.assertEqual(type(i), str)

    def test_from_dic(self):
        '''Test the generation of a object from a dic'''
        a = User()
        dic = a.to_dict()
        b = User(dic)
        self.assertNotEqual(a, b)
        self.assertEqual(type(b.created_at), datetime.datetime)
        self.assertEqual(type(b.updated_at), datetime.datetime)