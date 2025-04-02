"""
This script groups elements of an iterable by the result of applying a function to each element.
"""

def group_by(func, iterable):
    """
    Groups elements of an iterable based on the result of applying a function to each element.

    :param func: The function to apply to each element of the iterable.
    :param iterable: The iterable to process.
    :return: A dictionary where the keys are the results of applying the function, 
             and the values are lists of elements that produced the corresponding result.
    """
    set_of_results = set(map(func, iterable))  # Create a set of results (to avoid duplicates)

    # Iterate over all results in the set and apply a filter to the original iterable
    # to find all elements which satisfy the result
    return {result: [element for element in iterable if func(element) == result] for result in set_of_results}

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
