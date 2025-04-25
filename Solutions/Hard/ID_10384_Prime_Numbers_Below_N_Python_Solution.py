#Python Solutionm
def get_primes(n):
    """ 
    :type n: int
    :rtype: List[int]
    """
    output = []
    def isprime(num):
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
        
    for i in range(2,n):
        if isprime(i) == True:
            output.append(i)
    return output

