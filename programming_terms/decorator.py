# closure1 - inner_function()
# def outer_function(msg):
#     def inner_function():
#         print(msg)
#
#     return inner_function()
#
#
# # closure2 - inner_function1
# def outer_function1(msg):
#     def inner_function1():
#         print(msg)
#
#     return inner_function1
#
#
# outer_function('Hi')
# function = outer_function1('Hi')
# function()
from functools import wraps


# Decorators - Dynamically Alter The Functionality Of Your Functions
def decorator_function(outer_function):
    @wraps(outer_function)
    # Wraps - it wraps the original_function to wrapper_function
    def wrapper_function(*args, **kwargs):
        print('Before {0}'.format(outer_function.__name__))
        return outer_function(*args, **kwargs)

    return wrapper_function


def prefix_decorator(prefix):
    def decorator_function(outer_function):
        @wraps(outer_function)
        # Wraps - it wraps the original_function to wrapper_function
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Before {0}'.format(outer_function.__name__))
            return outer_function(*args, **kwargs)

        return wrapper_function

    return decorator_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method is executed before {0}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print('Displaying')


@prefix_decorator('LOG:')
def display_args():
    print('Displaying')


# can use both decorator so that it can call one decorator inside another based on order
@decorator_class
@decorator_function
def display_info(name, age):
    print('Displaying {0} and age {1}'.format(name, age))


# function = decorator_function(display)

# print(function.__name__)
# display_info("Jeevan", 16)
display_args()
