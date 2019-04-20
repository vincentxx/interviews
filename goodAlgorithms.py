
##########These are DP programing practice that I have done

#find common longest CONTINOUS sub sequence between the two such as strings, arrays, lists, etc by using DP
#0(mxn) space(mxn)
def longestCommonSubsequence (list1, list2):
    n = len(list1)
    m = len(list2)
    dp = [[0] * m for i in range(n)] #matrix [n,m]
    answer = int(0) #the length of common sub sequence
    endPosition = -1
    #using DP, init dp[0,i] and dp[j,0] as 0
    #dp[i,j] = { }
    for i in range(n):
        for j in range(m):
            if list1[i] == list2[j]:
                print(i, " ", j)
                dp[i][j] = dp[i-1][j-1] + 1 #we only care the cross on the matrix of the continous adjacent
                print(dp[i][j])
                if dp[i][j] > answer:
                    answer = dp[i][j]
                    endPosition = i;
    #find the string
    # commonString = ""
    # if (answer > 0):
    #     for i in range(answer):
    #         commonString += str(list1[endPosition - answer + i +1])

    #do this by slice
    commonString = list1[endPosition - answer +1: endPosition + 1]

    return str(answer) + " : " + ''.join(commonString)


#find common longest NOT CONTINOUS BUT IN ORDER sub sequence between the two such as strings, arrays, lists, etc. by using DP


#knapsack problem

#given array and number N: find subset of array which sums to N

def findSumN (arr, n):
    m = len(arr)
    dp = [ [0]* m for key in range(n+1)]
    answer = dict()
    for i in range(n+1):
        for j in range(m):
            answer[(i,j)] = []
            if i > arr[j] and j >= 1:
                # two case: 1. if selected then find the next dp[i - arr[j]][j-1] of the j - 1 items, case 2.
                #if dp[i - arr[j], j - 1] == -1 mean not possible, then dp[i][j] = -1 , not possible too
                #else if there is answer then dp[i][j] = true, answer [ i, j] = answer[i - arr[j], j - 1]
                if  dp[i - arr[j]][j-1] == 0: #if not select item j
                    dp[i][j]  =  dp[i][j-1]
                    answer[(i,j)] = answer[(i,j-1)]

                else: #if select item j
                    dp[i][j] = 1
                    answer[(i,j)] = answer[(i - arr[j],j-1)] + [arr[j]]
            elif i == arr[j]:
                dp[i][j] = 1
                answer[(i,j)] = [arr[j]]
    for item in dp:
        print(item)
    print(answer)
    listAnswer = list()
    for (i,j) in answer.keys():
        if (i==n) and len(answer[(i,j)]) != 0 and answer[(i,j)] not in listAnswer: #ignore empty, duplicate
            listAnswer.append(list(answer[(i,j)])) # [ [], [],..]
            #print(answer[(i,j)])

    return listAnswer  #return the list of subsets (the answer), Sum(subset) = N

##problem on Kattis uci contest
def kattisExactchange2():
    numTestCases = int(input())
    price = int(input())
    n = int(input()) #size
    arr = [0]* n
    for i in range(n):
        arr[i] = int(input())
    found = False
    payValue = price
    minNumCoins = 100000
    while not found:
        answer = findSumN(arr, payValue)
        if len(answer) == 0: #not found
            payValue +=1
        else:
            print(answer)
            for item in answer:
                if minNumCoins > len(item):
                    minNumCoins = len(item)
            found = True
    return str(payValue) + " " + str(minNumCoins)

# Main()
# if __name__ == '__main__':

    #array2D = [[[]] * 10 for i in range(5)]
    # array2D[0][1] = 100
    # print(array2D[0][1])
    #print(array2D)

    # list0 = [0] * 15
    # print(list0)
    #
    # list1 = list ("vincentxagohago")
    # list2 = list("voneentxagoiuvis")
    # print(longestCommonSubsequence(list1,list2))

    #dict1 = { (1,2): [2], (2,3): [4]}
    #print(dict1)
    #dict1[(1,2)] = [3,4,5,6]
    #dict1[(2,3)] = dict1[(1,2)] + [100]
    #print(dict1[(2,3)])

    #arr = [1,2,3,19, 14, 4,5,6,7,8,9,11, 12, 17, 21, 23,34 ]
    #print(findSumN(arr,33))
    # print(kattisExactchange2())


######################################################################### What i have done
#########################################################################

#google example practice
def solution(S, K):
    # write your code in Python 3.6
    answer = []
    n = len(S)
    count = 0
    for i in reversed(range(n)):
        if S[i] != "-" and count < K:
            answer.insert(0, S[i].upper())
            count += 1
        if count == K:
            if i != 0:
                answer.insert(0, '-')
            count = 0

    return ''.join(answer)


#https://leetcode.com/problems/sliding-window-maximum/
class Solution1:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = -999999
        answerList = []
        n = len(nums)
        for i in range(n):
            if i >= k - 1:
                # using dp: max = max { the current subproblem, or if selected nums[i]
                tmp = 0
                tmp = max(nums[i - k + 1:i + 1])
                # answer = tmp if tmp > answer else answer
                answerList.append(tmp)
                # if (i-k+1 >=0) and answer < (nums[i] - nums[i-k +1]):
                #     answer = answer nums[i] - nums[i-k +1]

        return answerList


# imagine that when window slides, at each current pointer position i, using idea of DP programming
# we know the max number of the prev window: prevMax, but the trick is to record the index of that max number as
# the distance how far from the current pointer. The purpose is we only lost the track if prevMax is removed by sliding
# window to 1 item, then this is the only case that we need to loop k on the current window to find again the prevMax
# and distance. The algorithm complexity is linear, unless worst case that the array is descending order.
class Solution2:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answerList = []
        MIN_INTEGER = -2147483648  # min of integer 4 bytes
        prevMax = MIN_INTEGER
        n = len(nums)
        distance = 0  # how far to the previous Max number from the current pointer i checking value

        for i in range(n):
            distance += 1  # every loop pointer is stay away +1 from the prevMax position
            if i <= k - 1:  # first window k: [0:k-1]
                if prevMax <= nums[i]:
                    prevMax = nums[i]
                    distance = 0
                if i == k - 1:
                    answerList.append(prevMax)

            else:
                # at the current pointer index i
                if nums[i] >= prevMax:
                    prevMax = nums[i]
                    distance = 0
                    answerList.append(prevMax)
                else:  # current value < prev window max
                    if distance == k:  # preMax stays at the boundary of the window and to be removed,
                        # reset to find it again in current window
                        prevMax = MIN_INTEGER
                        for j in range(k):
                            if prevMax < nums[i - j]:
                                prevMax = nums[i - j]
                                distance = j
                        answerList.append(prevMax)
                    else:
                        answerList.append(prevMax)

        return answerList

#https://www.techiedelight.com/list-of-problems/
#Arrays
#sort or partitioning 0, 1
#partitioning 0,1,2
#find Max length sub array(continuous) with given sum
#find duplicate with range n (using mod % n)
#Find maximum product of two integers in an array: sorted, then answer = either 2 max or 2 bottom negative
#

#binary tree, data structure


#way to think about the funciton as data, the code as data: VERY USEFUL IF WRAP UP SOMEBODY's CODE (FUNCTIONS)
def func1(x):
    def func2(y):
        return (x+y)
    return func2
#

myfunc = func1(1)
myfunc(2) # is 1+2 = 3

def binop(x,y,func):
    return func(x,y)
