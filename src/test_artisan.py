#!/usr/bin/env python

from __future__ import absolute_import, print_function

import unittest

import artisan
import tests.blueprints

class Foo(object):
    ''' Some Class '''

    def __init__(self, *args):
        name = None

class Bar(object):
    ''' Some Other Class '''

    def __init__(self, an_argument):
        self.random_attrib = an_argument
        self.name = None

artisan.prepare(tests.blueprints)

class TestArtisan(unittest.TestCase):

    def setUp(self):
        ''' Set up the tests '''
        pass

    def tearDown(self):
        ''' Tear Down the tests '''
        pass

    def test_instance_creation(self):
        for num in range(10):
            new_instance = artisan.craft(Foo)
            assert new_instance.name is not None

    def test_instance_creation_with_arguments(self):
        for num in range(10):
            name = "FooBarBaz_{}".format(num)
            new_instance = artisan.craft(Bar, num, name=name)
            assert new_instance.random_attrib == num
            assert new_instance.name == name

    def test_keyword_overrides(self):
        new_instance = artisan.craft(Foo, name='FooBarBaz')
        assert new_instance.name == 'FooBarBaz'
