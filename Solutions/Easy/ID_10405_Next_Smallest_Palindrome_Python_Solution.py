#Python Solution
#Since a Palindrome is involved, we'll have to use indexing and slicing of a string
#We use a for loop in this case, then convert the number to a string. If the reverse of that string is true, return that number
def next_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    for i in range(n+1,10000000):
        if str(i) == str(i)[::-1]:
            return i
