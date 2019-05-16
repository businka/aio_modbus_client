import asyncio
import inspect


def async_test(f):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        # kwargs['loop'] = loop
        if inspect.iscoroutinefunction(f):
            future = f(*args)
        else:
            coroutine = asyncio.coroutine(f)
            future = coroutine(*args, **kwargs)
        loop.run_until_complete(future)

    return wrapper
