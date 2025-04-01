def cup_of_join(*lists, sep = None):
    result = []

    for list in lists:  #append lists including the separator in the beginning
        result += list
        if sep != None:
            result.append(sep)

    return result if len(result) !=0 else None  #return not including the first separator or None if it's empty



if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6]))