from typing import List, Dict

#s = [1,2,3,4,5]

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


"""

#prepare for onsite interview: 2 weeks from now

# 2 Coding Interview
# System coding: text manipulation, handling input/output, automating tasks, interfacing with 
external systems/processes

################TEXT MANIPULATION 
## open a file and loop through each line:
with open(fileName, "r") as f:
    for line in f:
        ## do something each line
        
## using split to parsing the string
    string.split(',')
    string.split(', ')
    using re
##

######################### HANDLING INPUT/OUTPUT

how to handle stream in python as real, in case of the file is too big or is updated regularly (as the 'pipe' )


##################### AUTOMATING tasks????



######################## INTERFACE WITH external systems/process:

python call process, how python execute a command, etc. ????



#Strategy: find the most common task and practice (learn by heart) it - DONE

#Use bash/shell script with simple task, usually admin task
### see common commands, list down here:
grep, ls, cat, wc, awk, sed, for loop basic, if statement, trap, 
wget, git, open files, write files, pipe, 

pipe is concurrency
pssh, strace, 

[THINK ABOUT THE SCALABILITY] - DONE

#User python if it's hard for bash/shell script
spawn a subprocess
store a data structure when parsing file content (log file)
do http request and parsing its content
some common: string.split(), 
regular expression,
concurrency technique


##Coding based on algorithm and Data structures: DONE
Leetcode
Group problems into P, NP, to some dedicated problem such as:
Bin pack, Knapsack, Schedule Room, Tree traversal, Graph traversal,





# 1 System Interview: scenario, networking, kernel, troubleshooting, performance (Brendan)

### Verify performance, troubleshooting in quick, follow USE method from Brendan Gregg
vmstat
top/htop
iostat
netstat


### review detail in kernel space and kernel system call list
slides 143 OS DONE
slides from networking DONE
slides from 146: see how command really work from user space to kernel space DONE
slides from 53
slides from 161: greedy, dp, divide & conquer, trick-arrays, graph (topological, bfs, dfs, shortest path, etc.), binary search to speed up, hashmap(key:val) convernt O(n) to O(logn)
sdn paper review & print 3 copies
review "work note"
writing code on w-board DONE
performance eval - brendan, review the diagram


#Behavior interview

##talking about the research project and deploying openvpn by using puppet/, ideas of bastion host


"""


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




"""GLASSDOOR questions"""
#reimplement 'tail' in a scripting language

"""
Battleship game: write a function that finds a ship and return its coordinates.
 Write a script that connects to 100 hosts, looks for a particular process and sends an email with a report.
 What is a filesystem, how does it work? File permissions, properties, file types. A write operation failed with an error, how do you figure out what happened? What's a signal and how is it handled by the kernel? What's a zombie process?
 
 Talk about an iostat output (what does user vs system cpu load mean, what does iowait% mean, cache vs buffers, why do we need caching, how much cache is needed, how can disk performance be improved, where is the bottleneck)
 How do TCP, UDP work? Describe what happens when a client opens a web page. How does DNS work? How does HTTP work? How does a router work?
 Various questions about your current experience, talk about a conflict situation and how you handled it.
 How would you design a system that manipulates content sent from a client (e.g. clean bad words in a comment post)?
 Write a function to sort a list of integers that looks like this [5,2,0,3,0,1,6,0] -&gt; [1,2,3,5,6,0,0,0] in the most efficient way.

How can you find whether a process is I/O bound or CPU bound?

The interviewer had me to dig into the internals of operating system, such as performance tuning, memory model, paging, swap, process forking, system call, interrupt, and etc
Familiar with operating system internals and system analysis tools
 - Familiar with networks and infrastructures (TCP/IP, DNS, HTTP, and etc)
 - Think about scalability
 
 Why wouldn't you want a root DNS server to answer queries for you, instead of delegating you to an authoritative server?


For a given set of software checkins, write a program that will determine which part along the branch where the fault lies.

With very little detailed information, how would you approach tackling a performance problem in a web application (i.e., step through your thought process of what steps you would take, information you would seek, etc.).  
Write an algorithm to determine whether a string is a palindrome.

The process begins with an online pre-screening quiz, multiple choice questions about basic OS concepts and Linux tools.
 
 Then there are 2 phone interviews: coding and systems. Coding round is File I/O and data manipulation. Systems round they give you a troubleshooting scenario and make you drill-down on the topic.
 
 Finally, the onsite interview consists of four total rounds: 1 behavioral, 1 systems, and 2 coding rounds. Unfortunately, I had a bad day and choked on the coding rounds.
 Given a string, determine if it is a palindrome.
Given a file with multiple columns, print the first and the third column out and find a new value based on the values of those two columns.

Explain containerization?
What happens in Linux when you type ls -l?
Explain pagination(might be different wordings)

One question that is similar to one I got is "'httpd' is not serving files from '/var/www/html'. Why might this be happening? How might you go about diagnosing and fixing this?". Be sure to know exactly where your knowledge ends
We have a database running unusually slow in production. Why might this be happening?
Question about manipulating data from stdin and battleship problem.

The Bulb Switcher question you can find on Leetcode.

How would you handle processing large datasets in a constrained environment?

Goat latin
Given output of command vmstat and analyze the system.
Send packets to remote machines and try to upgrade the packet remotely. Troubleshooting why some of the machines are not updated.

What part of the tcp header does traceroute modify?

How do you make a process a service?

What is a zombie process?

Given a list of words, create a master list that has sublists that contain anagrams.

What happens during the boot process from the moment you turn on the machine until you get a login prompt?
Name three states a process can be in.


In IPv6 what is the A record equivalent?

What is the default signal that is generated when sending a kill command to a process in Linux?

when you saw many system interrupts, what could be the possible reason in linux



Round 2: coding
Question 1: Was given a string and check if we can rearrange the string as a palindrome
Question 2: input char array consistes of 'W' and 'H' for week day and holiday respectively, and an
int n
we can change 'W' to 'H' n times and return the longest continoust subarray consisting 'H'



What I feel is: Facebook will ask you to do simple tasks and think how they will run with large inputs. Everything that i code was asked “What about if this input is a file with 1TB?". So, when studying, don’t think you will need to know all data structures in your mind, but make sure you are fresh with the concepts of interacting with large inputs, optimization and system/network knowledgement.

Adding new Stage: Systems

I got busted new stage, but was really nice to have it. When come to Linux, i was pretty confident, but i got a surprise.

The interview started with “When i do $(ls -l foo*), tell me what’s happen from eletric signal from keyboard to Linux Kernel”

So i started talking about fork, syscalls, and the interview start digging:

“Which syscall you use to create a new process?”
“And for listing files?”
“The wildcard ‘*’ is implement on userspace or kernelspace”

Well, after this, i realize that this stage needs a complete understanding how to interact with Linux Kernel. So, i recomend try to answer the first question “How a simple command goes from keyboard to Linux Kernel” and be prepared to dig how long you know.
https://www.quora.com/How-should-I-prepare-for-a-production-engineer-interview-at-Facebook







"""


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


