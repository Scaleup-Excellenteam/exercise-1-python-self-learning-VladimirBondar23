"""
This script defines a function that joins multiple lists with an optional separator.
"""

def cup_of_join(*lists, sep = None):
    """
        Joins multiple lists into one, optionally inserting a separator between them.

        :param lists: Lists to be joined.
        :param sep: Separator to be inserted between lists (default: None).
        :return: The joined list or None if the result is empty.
        """
    result = []

    for lst in lists:  #append lists including the separator in the beginning
        result += lst
        if sep is not None:
            result.append(sep)

    return result if len(result) !=0 else None  #return not including the first separator or None if it's empty

if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
