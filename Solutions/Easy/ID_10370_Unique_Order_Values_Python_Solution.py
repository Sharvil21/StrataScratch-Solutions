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

#Another Python Solution
def non_duplicate(input):
    """ 
    :type input: List[int]
    :rtype: List[int]
    """
    
    seen = set()
    result = []
    
    for n in input:
        if n not in seen:
            seen.add(n)
            result.append(n)
            
    return result
    

