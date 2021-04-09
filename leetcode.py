from typing import List, Dict

#s = [1,2,3,4,5]
#sum += incr
#incr = 10* i + 15*j + 55*k
def print1000():
    f10,f15,f55 = True, False, False
    c55 = 0
    genSum = 0
    while genSum < 1000:
        print(genSum)
        if f55:
            genSum += 55
            f10,f15,f55 = True,False,False
        elif f10:
            genSum +=10
            f10,f15,f55 = False,True,False
        elif f15:
            genSum +=15
            c55 +=1
            if c55 == 2 : #reset
                f10,f15,f55 = False,False,True
                c55 = 0
            else:
                f10,f15,f55 = True,False,False
#print1000()

def print10000v2():
    cons = [(1,0,0), (0,1,0), (2,0,0), (1,1,0), (0,2,0), (2,1,0), (3,0,0), (3,1,0), (2,2,0), (0,0,1)]
    base = 0
    MAX = 1000
    while base < MAX:
        answer = 0
        incr = 0
        for (i,j,k) in cons:
            incr = 10*i + 15*j + 55 * k
            answer = base + incr
            if answer <= MAX:
                print(answer)
            else:
                return None
        base = answer

    return None


#print10000v2()

def genNumbers(x):
    curr =[]
    prev = ['0','1','2','3','4','5','6','7','8','9']
    DIGITS = ['0','1','2','3','4','5','6','7','8','9']
    for i in range (1,x):
        ## current = prev,each U (0,1,..9)
        curr = []
        for item in prev:
            for digit in DIGITS:
                curr.append(item + digit)
        prev = curr
    for i in curr:
        print(i)

    return None

#genNumbers(10)


def subSequence(s1: str, s2: str) -> str:
    n1 = len(s1)
    n2 = len(s2)
    # data structure
    # dp: {key: (i,j), val: []}
    dp = dict()
    for j in range(n2 + 1):
        dp[(0, j)] = []
    for i in range(n1 + 1):
        dp[(i, 0)] = []
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[(i, j)] = dp[(i - 1, j - 1)] + [s1[i-1]]
            else:
                # dp[(i,j)] = max(dp[(i,j-1)], dp[j-1,i])
                if len(dp[(i, j - 1)]) >= len(dp[(i - 1, j)]):
                    dp[(i, j)] = dp[(i, j - 1)]
                else:
                    dp[(i, j)] = dp[(i - 1, j)]

    return ''.join(dp[n1, n2])

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print(id(mylist))
   print ("Values inside the function: ", mylist)
   return

def test4(x):
    print(id(x))
    x +=1
    print(x)
    print(id(x))
    return None

def isSubsequence(s: str, t: str) -> bool:
    t = iter(t)
    return all(c in t for c in s)

# Now you can call changeme function
# mylist = [10,20,30]
# print(id(mylist))
# changeme( mylist )
# print ("Values outside the function: ", mylist)
#
#
# x = 3
# print(x, id(x))
# test4(x)
# print(x, id(x))
#
# print(subSequence("abcdsxaefda", "xacefdzdads"))
# print(isSubsequence("aaa", "xaadas"))
import copy
def generateSum(S, m, limit):
    basic = [0]*m
    prev = [basic]
    curr = []
    total = 0
    print(S)
    while total < S:
        #print(prev)
        curr = []
        for item in prev: #item = M-list
            for j in range(m):
                if item[j] < limit:
                    tmp = copy.copy(item)
                    tmp[j] +=1
                    if tmp not in curr:
                        curr.append(tmp)

        print("No:", curr)
        del prev[:]
        prev = curr
        total +=1

    a= list(map(lambda x: ''.join(map(str,x)), curr))
    print(a)
    a.sort(reverse=False)
    print(a)
    return None

#generateSum(10,4,9)

# test = [1,1,3,4,5,5,5,4,4,4,5,3]
# dic = dict()
# for i in set(test):
#     dic[i] = sum(map(lambda x: 1 if x==i else 0, test))
#     print(i, dic[i])
# print(dic)

def findMeetingRoom(intervals): #intervals = [(x,y), ....]

    #sorting by the finished time interval i
    #get the list of max items of none overlap sessions => mark it color 1
    #repeat
    #return the number of color
        interList = copy.copy(intervals)
        interList.sort(key= lambda x: x[0])
        color = -1
        print(interList)
        colorNum = []
        #colorNum[color] stores the latest ended time, color is the index starting at 0
        for i,v in enumerate(interList):
            matchColor = isCompatible(v,colorNum)
            if matchColor is not None: #check and set the ended time if yes
                print("--")
                colorNum[matchColor] = v[1]
                print("v,color", v, matchColor)
            else: #create new color
                color += 1
                colorNum.append(v[1])
                print("v,color", v, color)
                #colorNum[color] = v[1] #store the ended time
        return color+1

def isCompatible(item, colorNum): #return the color i if compatible
    if len(colorNum) == 0:
        return None
    else:
        for i in range(len(colorNum)):
            if colorNum[i] < item[0]:
                return int(i)
        return None


# intervals = [(1,4), (1,7), (1,4), (5,8), (5,16), (9,12), (9,12), (13,16), (13,16)]
# print("Answer: ", findMeetingRoom(intervals))

#
# 1,4 5,8 9,12 13,16
# 1,4 9,12
# 1,7
# 5,16

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Complexity O(n): Pass each item once
    n = len(nums)
    i, i1, i2 = 0, 0, n - 1  # red, white, yellow
    done = False
    if n == 1:
        return None
    while i <= i2 and not done:
        if nums[i] == 0:
            i += 1
        elif nums[i] == 2:
            # swap with i2
            while i2 > 0 and i2 > i and nums[i2] == 2:
                i2 -= 1
            tmp = nums[i2]
            nums[i2] = nums[i]
            nums[i] = tmp
            i2 -= 1
        elif nums[i] == 1:
            # look for the range i+1:i2 if there is not 1 then swap
            if i1 < i:
                i1 = i;
            while i1 <= i2 and nums[i1] == 1:
                i1 += 1
            if i1 > i2:  # done
                done = True
                break;
            else:
                tmp = nums[i1]
                nums[i1] = nums[i]
                nums[i] = tmp


def numIslands(self, grid: List[List[str]]) -> int:
    if len(grid) < 1:
        return None
    row = len(grid)
    col = len(grid[0])
    check = [[0] * (col + 1) for i in range(row + 1)]  # build matrix wrap around grid
    islandLabel = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if grid[i - 1][j - 1] == 1:
                # grid[i-1][j-1] is check[i][j]
                if check[i - 1][j] == 0 and check[i][j - 1] == 0:
                    # found new island
                    islandLabel += 1
                    check[i][j] = islandLabel
                else:
                    check[i][j] = max(check[i - 1][j], check[i][j - 1])

            print(check[i][j], end=" ")
        print()

    return islandLabel


class SolutionX:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # convert to tuple2, calculate the distance and sort it

        distance = dict()
        for i in points:
            tup2 = (i[0], i[1])
            dis = math.sqrt(i[0] ** 2 + i[1] ** 2)
            distance[tup2] = dis
        # sorted d by dis value
        sortedD = sorted(distance, key=lambda x: distance[x])
        sortedDistance = {i: distance[i] for i in sortedD}

        answer = list()
        count = 1
        for i in sortedDistance:
            if count <= K:
                item = [i[0], i[1]]  # tup2 to list2
                answer.append(item)
                count += 1
        return answer

#d = {(1,2): 3, (3,4):1}
#sort dictionary by values or function of it
#print(sorted(d, key= lambda x: d[x])) # x is the key of d because it is iterable by default

#sortedD = sorted(d,key= lambda x: d[x])
#d2 = {i:d[i] for i in sortedD}
#print(d2)

#oh my god stupid, here is short:
def kClosest(self, points, K):
    points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
    return points[:K] #important note: print without loop HAY HAY

#sorted a list by two attributes
l = [(0,1), (1,2), (0,2), (1,1)]
print(sorted(l,key = lambda x: (x[0], x[1])))

def subsets(nums):
    nums.sort()
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result


def subsets2(nums):
    dp = [[]]
    for num in nums:
        for i in copy.copy(dp):
            item = [num] + i
            dp.append(item)

    return dp

print(subsets2([1,2,3]))


def subarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = []  # list of sums that ended at j (which is check == k to count)
    count = 0
    answer = list()
    for i in nums:
        answer = []
        for item in dp:
            sub = item + i
            if sub == k:
                count += 1
            answer.append(sub)
        if i == k:
            count += 1
        answer.append(i)
        dp = answer
        # print(dp)

    return count

def subarraySum(self, nums: List[int], k: int) -> int:
    track = {0:1}
    total = 0
    count = 0
    for i in nums:
        total +=i
        if (total - k) in track:
            count += track[total-k]

        if total not in track:
            track[total] = 1
        else:
            track[total] +=1
        #print(track)
    return count

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



##Leetcode >> Facebook interviews common coding questions
#Find the longest substring with all characters DIFFERENT AND CONTINOUS >> Using the DP
'''
find the longest substring with all character different
algo: window slide: at the moment at string N, looking at next char X on N+1:
    1)choose
    2)not choose
'''
def lengthOfLongestSubstring(s:str):
    candidate = []
    temp = []
    for c in s:
        if c not in temp:
            temp.append(c)
        else:
            # add temp to candidate list
            candidate.append(''.join(temp))
            temp = getNewCandidate(temp, c)

    candidate.append(''.join(temp))
    print(candidate)
    return maxLengthOfElement(candidate)

def getNewCandidate(lst, c):
    tmp = []
    for i in range(len(lst)):
        if lst[i] == c:
            lst.append(c)
            tmp = lst[i + 1:]
            break
    return tmp

def maxLengthOfElement(candidate):
    maxTemp = 0
    for i in candidate:
        if maxTemp < len(i):
            maxTemp = len(i)
    return maxTemp

print(lengthOfLongestSubstring("abcaadslladxyaydiuaondsdced"))



#Roman to integer, intepreter a ROMAN characters to integers
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            x = s[i]
            if i != len(s) - 1:  # pos not at last char of the string
                y = s[i + 1]
            else:
                val = self.findVal(x, ' ')
                total += val[0]
                break

            val = self.findVal(x, y)  # return (val,1 or 2)
            if val[1] == 2:
                i += 2
            else:
                i += 1

            total += val[0]

        return total

    def findVal(self, x, y):  # return tuple (val,1 or 2)
        # constant mapping value dictionary
        convertNumber = {
            'I': 1,
            'II': 2,
            'III': 3,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        key = ''.join(x + y)
        if key in convertNumber.keys():
            return (convertNumber[key], 2)
        else:
            return (convertNumber[x], 1)


#is string palindrome?
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        # remove non alphabet chars
        regex = re.compile('[^a-zA-Z0-9]')
        # First parameter is the replacement, second parameter is your input string
        s2 = regex.sub('', s)
        # Out: 'abdE'
        s3 = s2.lower()

        # compare
        i = 0
        j = len(s3) - 1
        print(s3)
        while i < j:
            if s3[i] != s3[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

#Find X+Y+Z = n; using DP
def findSumXYZ(n) -> list:
    currentList=[]
    preList=[(0,0,0)]
    i=1
    while i <= n:
        currentList = buildFrom(preList)
        preList = currentList
        i +=1
    return currentList

def buildFrom(preList: list):
    result = []
    print(preList)
    for item in preList:    #each item is (X,Y,Z)
        #todo need to check duplicated before add item

        result.append((item[0]+1, item[1], item[2]))
        result.append((item[0], item[1]+1, item[2]))
        result.append((item[0], item[1], item[2]+1))
    return result

#print(findSumXYZ(3))


class Solution02:
    def letterCombinations(self, digits: str):
        letters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        combination = []

        def findList(resultStr, index) -> str:
            if len(resultStr) == len(digits):  # accept
                combination.append(resultStr)
                return None

            for aLetter in letters[digits[index]]:
                tmp = resultStr + aLetter
                findList(tmp, index + 1)
            return None

        findList("", 0)
        print(combination)
        return combination

#test= Solution02()
#test.letterCombinations('23')


class Solution03:
    def permute(self, nums: list) -> list:
        def findPermutation(nums) -> list:
            if len(nums) > 1:
                tmp = nums[0:(len(nums) - 1)]
                lastNum = nums[len(nums) - 1]
                subResult = findPermutation(tmp)
                # build a new list of permutation based on the lastNum and the sub result list
                return buildNewPermutation(lastNum, subResult)
            else:
                return [nums]

        def buildNewPermutation(lastNum, subResult): #[[]]
            result = []
            for item in subResult:
                for i in range(len(item)+1):
                    tmp = item.copy()
                    tmp.insert(i,lastNum)
                    result.append(tmp)
            return result



        print(findPermutation(nums))

# test= Solution03()
# test.permute([1,2])


class Solution05:
    def removeInvalidParentheses(self, s: str) -> list:
        # generate the f(string n) from f(string n-1)
        def generateS(s: str) -> list:
            result = []
            #
            if len(s) == 1:
                # do something to stop
                result.append(s)
                result.append("")
            else:
                firstChar = s[0]
                subStr = s[1:len(s)]
                subResult = generateS(subStr)
                # build result from sub result by either choose or not choose firstChar
                for item in subResult:
                    tmp = firstChar + item
                    result.append(tmp)
                if firstChar == "(" or firstChar == ")":
                    result.extend(subResult)
            print(result)
            return result
        master = generateS(s)

        #def validate(s:str)->boolean:
        def validate(s:str) -> bool:
            flag = 0
            for item in s:
                if item == "(":
                    flag +=1
                elif item == ")":
                    flag -=1

                if flag < 0:
                    return False
            if flag > 0 or flag < 0:
                return False

            return True

        #validate
        result=[]
        max = 0
        for item in master:
            if validate(item):
                if max < len(item):
                    max = len(item) #found a long list so reset it
                    result = []
                    result.append(item)
                elif max == len(item):
                    if item not in result:
                        result.append(item)
        print("final result:\n")
        print(result)
        return result

# test= Solution05()
# test.removeInvalidParentheses(")(")


class Solution06:           #using Recursive
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generateSubset(nums: List[int]) -> List[List[int]]:
            result = []
            if len(nums) == 1:
                # do something when stop recursive here:
                tmp = [nums[0]]
                result.append(tmp)
                result.append([])
                # return result [[],[x]]
            else:

                lastChar = nums[len(nums) - 1]
                subResult = generateSubset(nums[0:len(nums) - 1])

                # build result from subresult
                for item in subResult:
                    tmp = item.copy()
                    tmp.append(lastChar)
                    if tmp not in subResult:
                        result.append(tmp)
                    result.append(item)
            print(result)
            return result

        return generateSubset(nums)


class Solution07:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generateSubset(nums: list[int]) -> list[list[int]]:
            if len(nums) == 0:
                return []
            else:
                sub1 = [[], [nums[0]]]  # DP1,
                pre = sub1
                current = sub1
                for i in range(2, len(nums) + 1):  # 2 to n
                    # build current from pre
                    currentChar = nums[i - 1]
                    current = []
                    for item in pre:
                        tmp = item.copy()
                        tmp.append(currentChar)
                        if tmp not in current:
                            current.append(tmp)
                        current.append(item)

                    # DP:assign back for next round
                    pre = current
                return current

        return generateSubset(nums)

