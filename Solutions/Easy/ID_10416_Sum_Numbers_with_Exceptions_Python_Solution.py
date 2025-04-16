#Python Solution
#I just used the sum() function with list comprehension
#For the list comprehension, I had to use 'and' operator in the if condition as both conditions must be true to add the number into the list
def calculate_sum(N):
    """ 
    :type N: int
    :rtype: int
    """
    return sum([i if (i%3 != 0 and i%7 !=0) else 0 for i in range(0,N+1)])
