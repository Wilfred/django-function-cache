**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Installing](#installing)
- [Usage](#usage)
- [Alternatives](#alternatives)
- [Changelog](#changelog)
	- [v1.1](#v11)
	- [v1.0](#v10)
- [Developing](#developing)
	- [Releasing a new version](#releasing-a-new-version)

## Installing

    $ pip install django_function_cache

## Usage

Simply wrap `cached` around your expensive function:

    from urllib2 import urlopen
    import json

    from django_function_cache import cached


    def get_external_ip():
        response = urlopen("http://httpbin.org/ip").read()
        ip = json.loads(response)['origin']
        return ip


    def print_my_ip():
        print cached(get_external_ip)()

You can also specify a timeout:

    def print_my_ip():
        print cached(get_external_ip, minutes=5)()

You can specify any time units
[supported by timedelta](http://docs.python.org/2/library/datetime.html#datetime.timedelta).

If the wrapped function raises an exception, nothing is cached and the
exception propagates as if you'd call the function directly.

## Alternatives

If you're just caching database calls, you're probably better off
using
[Johnny Cache](http://pythonhosted.org/johnny-cache/index.html).

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
