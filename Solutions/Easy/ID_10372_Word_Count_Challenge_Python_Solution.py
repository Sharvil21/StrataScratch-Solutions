##Python Solution using .split() method
def count_words(sentence):
    """ 
    :type sentence: str
    :rtype: int 
    """
    return len(sentence.split())

#Another Python Solution
def count_words(sentence):
    words = sentence.split()
    return len(words)
