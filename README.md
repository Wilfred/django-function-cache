A simple wrapper for slow functions.

    >>> def foo(x): print "called"; return 1
    >>> cached(foo)('whatever')
    called
    1
    >>> cached(foo)('whatever')
    1

We cache based on the function name, its module name, and the
arguments.

MIT license, see COPYING for details.
