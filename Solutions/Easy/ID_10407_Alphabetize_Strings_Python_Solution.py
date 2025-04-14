#Python Solution
def sort_string(string):
    """
    :type string: str
    :rtype: str
    """
    return "".join(sorted(string))

#In the above solution, use the sorted() function to sort the string. But this will first put the alphabets in a list then sort it.
#So to get the desired string back, use the "".join() method and return it
