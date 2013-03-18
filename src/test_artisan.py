#!/usr/bin/env python

from __future__ import absolute_import, print_function

import unittest

import artisan
import tests.blueprints
import tests.models

artisan.prepare(tests.blueprints)

class TestArtisan(unittest.TestCase):

    def setUp(self):
        ''' Set up the tests '''
        pass

    def tearDown(self):
        ''' Tear Down the tests '''
        pass

    def test_instance_creation(self):

        new_instance = artisan.craft(tests.models.Foo)

        self.assertIsInstance(new_instance, tests.models.Foo)
        self.assertIsNotNone(new_instance.name)

    def test_instance_creation_with_arguments(self):

        new_instance = artisan.craft(tests.models.Bar, 42)

        self.assertIsInstance(new_instance, tests.models.Bar)
        self.assertEqual(new_instance.random_attrib, 42)

    def test_keyword_overrides(self):

        new_instance = artisan.craft(tests.models.Foo, name='FooBarBaz')

        self.assertIsInstance(new_instance, tests.models.Foo)
        self.assertIsNotNone(new_instance.name)
        self.assertEqual(new_instance.name, 'FooBarBaz')


if __name__ == '__main__':
    unittest.main()
