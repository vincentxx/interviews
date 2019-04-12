#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#

def minimalOperations(words):
    result = []
    for word in words:
        n = len(word)
        answer = 0
        if n >= 2:
            common = '$' #special
            for i in range(n):
                if i>0 and word[i] == word[i-1]:
                    if word[i] != common:
                        answer += 1
                        common = word[i]
                        #print(word, " ", common)
                    else:
                        common = '$' #reset after detect xxx
                else:
                    common = '$' #reset
        else:
            answer = 0;
        result.append(int(answer))
    pass
    return result
    # Write your code here

if __name__ == '__main__':

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the braces function below.
def braces(values):
    # algorithm ideas: using the stack to cancel the braces
    cancel = {'{': '}', '[': ']', '(': ')'}
    answers = []
    for value in values:
        n = len(value)
        stack = []
        found = 'YES'
        for i in range(n):
            if value[i] == '{' or value[i] == '[' or value[i] == '(':
                stack.append(value[i])
            else:
                if len(stack) != 0:  # stack not empty
                    item = stack.pop()
                    if cancel[item] != value[i]:  # detected problem
                        found = 'NO'
                        break
                else:
                    found = 'NO'
                    break

        if len(stack) != 0:
            found = 'NO'

        answers.append(found)

    return answers


if __name__ == '__main__':

    # !/bin/python3

    import math
    import os
    import random
    import re
    import sys


    #
    # Complete the 'decode' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING_ARRAY codes
    #  2. STRING encoded
    #

    def decode(codes, encoded):
        # store codes into hastable dictionary
        translate = dict()
        for item in codes:
            tmp = item.split('\t', maxsplit=1)
            if len(tmp) != 0:
                translate[tmp[1]] = tmp[0]

        print(translate)

        # traverse the encoded and slice to decode
        start = 0
        n = len(encoded)
        answer = []
        for i in range(1, n + 1, 1):
            check = encoded[start:i]
            if check in translate.keys():  # found
                if translate[check] == '[newline]':
                    answer.append('\n')
                else:
                    answer.append(translate[check])
                start = i

        answerString = str()
        for i in answer:
            answerString += str(i)
        print(answerString)
        return answerString


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        codes_count = int(input().strip())

        codes = []

        for _ in range(codes_count):
            codes_item = input()
            codes.append(codes_item)

        encoded = input()

        result = decode(codes, encoded)

        fptr.write(result + '\n')

        fptr.close()
