#Python Solution
#Just gotta use string indexing and slicing directly to get the output
def is_palindrome(s):
    """ 
    :type s: str
    :rtype: bool
    """
    return s == s[::-1]
