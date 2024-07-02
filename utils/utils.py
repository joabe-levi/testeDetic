from functools import wraps


def cached_method(func):
    cache_name = f"_{func.__name__}_cache"

    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})

        cache = getattr(self, cache_name)
        key = (args, frozenset(kwargs.items()))

        if key not in cache:
            cache[key] = func(self, *args, **kwargs)

        return cache[key]

    return _wrapper
