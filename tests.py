# set up dummy settings
# this needs to happen before we import django_function_cache
from django.conf import settings
settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }
})
from django.test import TestCase
from django.core.cache import cache

from time import sleep

from django_function_cache import cached


class EnvironmentTest(TestCase):
    def test_memcached_running(self):
        """Ensure memcache is running.

        Several of our test fail if memcached isn't running, so this
        test checks the local environment is correct.

        """
        cache.set('foo', 'bar')
        self.assertEqual(cache.get('foo'), 'bar')


class CachedTest(TestCase):
    def setUp(self):
        super(CachedTest, self).setUp()
        cache.clear()
    
    def test_cache_returns_correct_value(self):
        def wrap_this_func():
            return "foo"

        self.assertEqual(cached(wrap_this_func)(), "foo")

    def test_function_not_called_twice(self):
        times_called = [0]
        def wrap_this_func():
            times_called[0] += 1

        cached(wrap_this_func)()
        cached(wrap_this_func)()

        self.assertEqual(times_called[0], 1)

    def test_expiry_time(self):
        times_called = [0]
        def wrap_this_func():
            times_called[0] += 1

        cached(wrap_this_func, seconds=1)()
        sleep(1.5)
        cached(wrap_this_func, seconds=1)()

        self.assertEqual(times_called[0], 2)

    def test_different_args_not_cached_together(self):
        times_called = [0]
        def wrap_this_func(x):
            times_called[0] += 1

        cached(wrap_this_func)("something")
        cached(wrap_this_func)("something else")

        self.assertEqual(times_called[0], 2)
