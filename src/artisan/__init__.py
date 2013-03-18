# Future Imports
from __future__ import absolute_import, print_function

# Standard Library Imports
# ...

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

    crafted_instance = klass(*args)

    for attribute, value in plan(klass, **kwargs).iteritems():
        if not tools.is_attr_set(crafted_instance, attribute):
            setattr(crafted_instance, attribute, value)

    return crafted_instance


def plan(klass, *args, **kwargs):
    ''' Create a hash with similar properties as a crafted class. '''

    planned_instance = {}
    planned_instance.update(__blueprints_by_klass(klass.__name__))
    planned_instance.update(kwargs)

    return planned_instance
