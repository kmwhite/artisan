#!/usr/bin/env python

import artisan
import blueprints

class Foo(object):
    ''' Some Class '''
    name = None

artisan.prepare(blueprints)

print('Testing instance creation')
for num in range(10):
    new_instance = artisan.craft(Foo)
    print(new_instance.name)

print('Testing Keyword Overrides')
for num in range(10):
    new_instance = artisan.craft(Foo, name='FooBarBaz')
    print(new_instance.name)


