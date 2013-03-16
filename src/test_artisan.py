#!/usr/bin/env python

from __future__ import absolute_import, print_function

import artisan
import tests.blueprints

# Testing simple class creation
class Foo(object):
    ''' Some Class '''

    def __init__(self, *args):
        name = None

artisan.prepare(tests.blueprints)

print('Testing instance creation')
for num in range(10):
    new_instance = artisan.craft(Foo)
    assert new_instance.name is not None

print('Testing Keyword Overrides')
for num in range(10):
    new_instance = artisan.craft(Foo, name='FooBarBaz')
    assert new_instance.name == 'FooBarBaz'

# Testing more complex class creation
class Bar(object):
    ''' Some Other Class '''

    def __init__(self, an_argument):
        self.random_attrib = an_argument
        self.name = None

print('Testing class creation')
for num in range(10):
    name = "FooBarBaz_{}".format(num)
    new_instance = artisan.craft(Bar, num, name=name)
    assert new_instance.random_attrib == num
    assert new_instance.name == name
