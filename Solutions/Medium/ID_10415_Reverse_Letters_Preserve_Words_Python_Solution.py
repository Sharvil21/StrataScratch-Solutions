#Python Solution
#Approach is to first split the string into a list, using .split() method
#Then iterate through a for loop.
#Then add the reverse of the iteration every time into an empty list (use .append() method)
#Lastly, use the .join() method to construct the required string which is the output
def reverse_letters(input_string):
    """ 
    :type input_string: str
    :rtype: str
    """
    op = []
    for i in input_string.split():
        op.append(i[::-1])
    
    return " ".join(op)
