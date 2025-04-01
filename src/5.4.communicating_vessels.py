from itertools import zip_longest
def interleave(*iterables):
    # Use zip_longest to handle unequal length iterables and fillvalue=None
    zipped = zip_longest(*iterables, fillvalue=None)

    # Extract elements from tuples and filter out the None values
    return [item for tup in zipped for item in tup if item is not None]


def generator_interleave(*iterables):
    # Use zip_longest to handle unequal length iterables and fill with None by default
    for tup in zip_longest(*iterables, fillvalue=None):
        for item in tup:
            if item is not None:  # Skip None values
                yield item

if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    gen_version = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen_version:
        print(element)