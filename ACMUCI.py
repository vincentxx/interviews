

def octToHex(n):
    s =  '0o' + str(n)
    print(s)
    intNum = int(s)
    print(hex(intNum))
    return None

def longestCommonSubsequence (list1, list2):
    n = len(list1)
    m = len(list2)
    dp = [[0] * m for i in range(n)] #matrix [n,m]
    answer = int(0) #the length of common sub sequence
    endPosition = -1
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
    commonString = ""
    if (answer > 0):
        for i in range(answer):
            commonString += str(list1[endPosition - answer + i +1])

    return commonString


def test(str1, str2):
    if len(str1) > len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    if str1 not in str2:
        return False

    return True


def bingItOn():
    n = int(input())
    array = []
    # for i in range(n):
    #     array.append(str(input()))

    answer = [0] * n
    for i in range(n):
        array.append(str(input()))
        if i >= 1:
            for j in range(i):
                # if check two of them is ok, then i is sub of j, so mark[i] = mark[j]+1
                # print(array[i], "  ", array[i-j-1])
                if test(array[i], array[i - j - 1]):
                    if answer[i - j - 1] != 0:
                        answer[i] = answer[i - j - 1] + 1
                        break
                    else:
                        answer[i] += 1

        print(answer[i])

    # for item in answer:
    #     print(item)
    return None

def arithmetic():
    line = input()
    n = len(line)
    base = 1
    total = int(0)
    for i in reversed(range(n)):
        total += int(line[i]) * base
        base *= 8

    answer = hex(total)
    print(answer[2:len(answer)])
    return None

if __name__ == '__main__':
    #bingItOn()
    arithmetic()