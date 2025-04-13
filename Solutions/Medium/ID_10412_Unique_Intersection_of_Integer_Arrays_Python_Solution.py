#Python Solution
def find_intersection(input):
    """ 
    :type input: Dict[str, List[int]]
    :rtype: List[int]
    """

    arr1 = input["arr1"]
    arr2 = input["arr2"]
    
    op = []
    for i in arr1:
        if i in arr2:
            op.append(i)
    return list(set(op))

#Another Python solution
def find_intersection(input):
    """ 
    :type input: Dict[str, List[int]]
    :rtype: List[int]
    """

    arr1 = input["arr1"]
    arr2 = input["arr2"]
    
    return list(set(arr1) & set(arr2))
