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


def 


#print(first_last('shjdhjsd'))
#print(even_odd_sums([10, 20, 30, 40, 50, 60]))
