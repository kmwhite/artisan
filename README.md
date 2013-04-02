### Artisan Testing

#### Installing Artisan
Installing is nice and simple. It is available in PyPI.

    pip install artisan

If you are not using a virtualenv, you probably will want to add the '--user' flag. However, you will also probably want to *start* using virtualenvs. Seriously, they're awesome.

#### Using Artisan
Let's assume there is a simple app you need to test with the Foo class. The Foo class looks a lot like:

    class Foo(object):
        ''' This is a simple object '''
    
        def __init__(self):
            self.name = None

Before you can use artisan, you need to setup blueprints. Blueprints are simply dictionaries that contain lambdas used to generate the random data. In my example, I use the great [python-faker](https://github.com/redneckbeard/python-faker) library (it is available on PyPI, but I find the git repo is far more current).

In 'blueprints.py':

    import faker
    
    Foo = {
      'name': lambda: faker.name.name(),
    }

In your tests, you then do:

    import blueprints
    import artisan
    
    artisan.prepare(blueprints)
    
    artisan.craft(Foo)                # Creates an instance of the Foo class with a randomly generated name
    artisan.craft(Foo, name='BarBaz') # Creates an instance of the Foo class with the name BarBaz

### A Complete Example

    Python 3.3.0 (default, Mar 13 2013, 18:04:53) 
    [GCC 4.2.1 20070719 ] on openbsd5
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import blueprints
    >>> import artisan
    >>> 
    >>> class Foo(object):
    ...     def __init__(self):
    ...         self.name = None
    ... 
    >>> 
    >>> artisan.prepare(blueprints)
    >>> artisan.craft(Foo).name
    'Mrs. Savion Kuhn'
    >>> artisan.craft(Foo).name
    'Ms. Pearlie Collier'
    >>> type(artisan.craft(Foo))    
    <class '__main__.Foo'>

### Miscellaneous
I've been trying to keep artisan Python3 and Python2.X compatible. Also, Artisan in no way replaces your testing library, but helps to craft better data to test with. There are a number of improvements I'd like to integrate as well:

 * I want to make the use of blueprints an optional component. Given a class to create, it would be cool to do introspection and determine the attributes to generate information for.
 * I want abstract calls to python-faker behind a fabricate submodule to make it easier for developers to use, namely not having to write out lambdas. Although lambdas are a fantastic tool, and incredibly powerful, not everyone knows them and we're supposed to target the '90% Use Case'.

### Disclaimer
Artisan is very much a Work In Progress. It will likely change. I am more than happy to accept Pull Requests, complaints, or general criticisms. Feel free to submit them on the GitHub repo.

## License ##
Copyright (c) 2012, Kristofer M White
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the software nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### References
 * [Artisan Github Repo](http://github.com/kmwhite/artisan)
 * [Artisan on PyPI](https://pypi.python.org/pypi/artisan)
 * [A review of Mocking](http://www.voidspace.org.uk/python/articles/mocking.shtml)
