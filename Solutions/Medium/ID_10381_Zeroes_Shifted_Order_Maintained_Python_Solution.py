#Python Solution
#There is no specific requirement to change the order in place, or anything as such
#So I use list comprehension to just add the non-zero numbers first. They are in order
#Then iterate through a for loop and add zeroes to the end using the .append() method
def shift_zeroes(arr):
    """ 
    :type arr: List[int]
    :rtype: List[int]
    """
    op = [i for i in arr if i != 0]
    for i in arr:
        if i == 0:
            op.append(i)
    return op
