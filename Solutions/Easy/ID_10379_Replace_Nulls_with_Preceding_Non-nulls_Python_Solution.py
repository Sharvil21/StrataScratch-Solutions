#Python Solution
#No need for special functions. A simple for loop will suffice
def replace_null_values(lst):
    """ 
    :type lst: List[Union[int, None]]
    :rtype: List[Union[int, None]]
    """
    for i in range(1,len(lst)):
        if lst[i] == None:
            lst[i] = lst[i-1]
    return lst
