"""
This script measures the execution time of a given function.
"""

import time

def running_2000(f, *args, **kwargs):
    """
    Measures the execution time of a function.

    :param f: Function to be executed.
    :param args: Positional arguments for the function.
    :param kwargs: Keyword arguments for the function.
    :return: Time taken to execute the function in seconds.
    """
    start_time = time.time()
    f(*args, **kwargs)  # Apply function and measure time difference
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    print(running_2000(str.format, "Hi {name}", name="Bug"))
