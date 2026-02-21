# import time


# def cache(func):
#     cache_value = {}
#     print(cache_value)

#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result  # It is to
#         return result

#     return wrapper


# @cache
# def long_running_func(a, b):
#     time.sleep(4)
#     return a + b


# print(long_running_func(4, 5))
# print(long_running_func(4, 5))
# print(long_running_func(2, 3))
############################################################################
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"Calling: {func.__name__} with args [{args_value}] and kwargs [{kwargs_value}]"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def add(a, b):
    return a + b


result = add(5, 10)  # These are integers!
print(f"Result: {result}")
