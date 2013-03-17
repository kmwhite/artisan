# Future Imports
from __future__ import absolute_import, print_function

# Standard Library Imports
import pprint
import sys

# Third Party Imports
import faker

# Local Imports
import artisan.tools

# artisan.blueprints is a placeholder for the module that has the
# classes defined for crafting. It contains hashes who's names
# match with the name of a type
blueprints = None

def __blueprints_by_klass(klass_name):
    ''' Fetch the hash from the blueprints '''
    # Rather than checking hasattr(), I'm trusting people not to
    # mess up. If people are right more often than not, we skip
    # a call to a function.
    return getattr(blueprints, klass_name)

def prepare(blueprints_module):
    ''' Prepare blueprints for testing '''
    global blueprints
    blueprints = blueprints_module

def craft(klass, *args, **kwargs):
    ''' Create, and return, an instance of klass. The value that are
        passed in via kwargs will override anything generated.
    '''
    # TODO - Change this to use artisan.plan() to generate a dictionary.
    # Then, use klass(*args).__dict__.update(instance_plan) to change the
    # attributes on it.
    crafted_instance = klass(*args)

    kwarg_keys = list(kwargs.keys())

    known_attrs = __blueprints_by_klass(str(klass.__name__))

    for attribute in list(known_attrs.keys()):
        if attribute not in kwarg_keys:
            if not tools.is_attr_set(crafted_instance, attribute):
                setattr(crafted_instance, attribute,
                        known_attrs[attribute]())

    for attribute in kwarg_keys:
        setattr(crafted_instance, attribute, kwargs[attribute])

    return crafted_instance


def plan(klass, *args, **kwargs):
    ''' Create a hash with similar properties as a crafted class. '''

    planed_instance = {}

    for attribute in known_attrs.keys():
        if attribute not in kwarg_keys:
            setattr(crafted_instance, attribute,
                    known_attrs[attribute]())

    for attribute in kwarg_keys:
        setattr(crafted_instance, attribute, kwargs[attribute])

    return planned_instance
