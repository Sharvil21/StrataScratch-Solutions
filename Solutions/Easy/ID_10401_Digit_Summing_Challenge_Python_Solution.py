#Python Solution
def sum_digits(numbers):
    """ 
    :type numbers: List[int]
    :rtype: List[int]
    """
    ip = [i if i>0 else i*-1 for i in numbers]
    op = []
    for i in ip:
        x = 0
        for j in str(i):
            x += int(j)
        op.append(x)
    return op
