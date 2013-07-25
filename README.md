A simple wrapper for slow functions.

    >>> from django_function_cache import cached
    >>> def foo(x): print "called"; return 1
    >>> cached(foo)('whatever')
    called
    1
    >>> cached(foo)('whatever')
    1

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
