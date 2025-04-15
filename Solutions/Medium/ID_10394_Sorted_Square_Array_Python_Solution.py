#Python Solution
#In this, I just used List Comprehension
def sorted_squares(arr):
    """ 
    :type arr: List[int]
    :rtype: List[int]
    """
    return sorted([i*i for i in arr])
