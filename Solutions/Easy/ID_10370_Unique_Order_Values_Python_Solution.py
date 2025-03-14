#Python Solution
def non_duplicate(input):
    """ 
    :type input: List[int]
    :rtype: List[int]
    """
    lst = []
    for i in input:
        if i not in lst:
            lst.append(i)
            
    return lst

#
