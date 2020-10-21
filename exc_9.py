def first_last(item):
    """ Takes a sequence (string, list, or tuple) and returns the first and 
        last elements of that sequence, in a two-element sequence of the same type
    """
    # first_element = item[0]
    # last_element = item[len(item) - 1]
    # if type(item) == list:
    #     return [first_element, last_element]
    # if type(item) == tuple:
    #     return (first_element, last_element)
    # if type(item) == str:
    #     return first_element + last_element

    # return item[:1] + item[-1:] 
    
    return item[0 : len(item) : len(item)-1]


def even_odd_sums(seq):
    """ Returns a two-element list, containing (respectively) the sum of the 
        even-indexed numbers and the sum of the odd-indexed numbers
    """
    even = seq[0::2]
    odd = seq[1::2]
    return [sum(even), sum(odd)]


def plus_minus(seq):
    """ Return the result of alternately adding and subtracting numbers from each other
        [10, 20, 30, 40, 50, 60])   10+20-30+40-50+60
    """
    items = even_odd_sums(seq)
    res = items[0] - seq[0]*2
    return items[1] - res


def myzip(*iterables):
    """ takes any number of iterables and returning a list of tuples. Each tuple
        contains one element from each of the iterables passed to the function
        Assume that all of the iterables are of the same length.
    """
    result_list = []
    for i in range(len(iterables[0])):  
        lst = []
        for k in iterables:
            lst.append(k[i])
        result_list.append(tuple(lst))
    return result_list


def mysum(*args):
    """ exercise 10
    """
    if not args:
        return args
    first = args[0]
    # for i in range(1, len(args)):
    #     first += args[i]
    for i in args[1:]:
        first += i
    return first


print(mysum())
#print(myzip([10, 20,30], 'abc', (1, 2, 3)))
#print(plus_minus([10, 20, 30, 40]))
#print(first_last('shjdhjsd'))
#print(even_odd_sums([10, 20, 30, 40, 50, 60])
