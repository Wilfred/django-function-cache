A simple wrapper for slow functions.

    In [1]: from django_function_cache import cached

    In [2]: def expensive_function(x): print "doing something slow!"; return 1

    In [3]: cached(expensive_function)('foo')
    doing something slow!
    Out[3]: 1

    In [4]: cached(expensive_function)('foo')
    Out[4]: 1

    In [5]: cached(expensive_function)('bar')
    doing something slow!
    Out[5]: 1

    In [6]: cached(expensive_function)('bar')
    Out[6]: 1

We cache based on the function name, its module name, and the
arguments.

MIT license, see COPYING for details.

## Installing

    $ pip install django_function_cache

## Changelog

### v1.1

Changed the top level package name. Previously you would write:

    from cached import cached

Now:

    from django_function_cache import cached

### v1.0

Initial release.

## Developing

Check out the code, and install it in a virtual environment that
includes Django:

    $ source path/to/your/virtualenv
    $ pip install -e .

Hack away, then send a pull request when you're happy.

### Releasing a new version

    $ python setup.py sdist upload
