"""
This script provides two functions to interleave multiple iterables:
- `interleave`: Returns a list of interleaved elements.
- `generator_interleave`: A generator version that yields interleaved elements one by one.
"""

from itertools import zip_longest

def interleave(*iterables):
    """
    Interleaves multiple iterables, skipping None values.

    :param iterables: Any number of iterables.
    :return: A list containing interleaved elements.
    """
    # Use zip_longest to handle unequal-length iterables and fill with None
    zipped = zip_longest(*iterables, fillvalue=None)

    # Extract elements from tuples and filter out None values
    return [item for tup in zipped for item in tup if item is not None]

def generator_interleave(*iterables):
    """
    Generator that interleaves multiple iterables, skipping None values.

    :param iterables: Any number of iterables.
    :yield: Interleaved elements one by one.
    """
    # Use zip_longest to handle unequal-length iterables and fill with None by default
    for tup in zip_longest(*iterables, fillvalue=None):
        for item in tup:
            if item is not None:  # Skip None values
                yield item

if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    gen_version = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen_version:
        print(element)
