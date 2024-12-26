#Python Solution
#Have to use the Counter from collections library
from collections import Counter
def non_repeated_words(input):
    """
    :type input: List[str]
    :rtype: List[str]
    """

    sentence1 = input[0]
    sentence2 = input[1]
    count = Counter(sentence1.split() + sentence2.split())
    output = []
    for i in count:
        if count[i] == 1:
            output.append(i)
    return output
