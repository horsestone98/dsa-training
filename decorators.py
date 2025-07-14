# Decorators are a powerful and flexible way to modify or extend the behavior of the functions or methods without changing their actual code.

# used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

def get_sprinkles(func):                            # First decorator function
    def wrapper(*args, **kwargs):
        print("Here is your sprinkles")
        func(*args, **kwargs)
    return wrapper

def get_fudge(func):                                # Second decorator function
    def wrapper(*args, **kwargs):
        print("Here is your fudge")
        func(*args, **kwargs)
    return wrapper

@get_sprinkles                                      # Calling decorator function 1
@get_fudge                                          # Calling decorator function 2


def get_ice_cream(flavor):                          # Base function
    print(f"Here is your {flavor} ice cream")

get_ice_cream("blueberry")