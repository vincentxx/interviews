
s = [1,2,3,4,5]

def print10000():
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

#print10000()

#sum += incr
#incr = 10* i + 15*j + 55*k
#100 010 200 110 020 210 220 001 -> repeat

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


intervals = [(1,4), (1,7), (1,4), (5,8), (5,16), (9,12), (9,12), (13,16), (13,16)]
print("Answer: ", findMeetingRoom(intervals))

#
# 1,4 5,8 9,12 13,16
# 1,4 9,12
# 1,7
# 5,16