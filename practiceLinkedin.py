##http request
import urllib.request
import http.client
import re

def makeSampleHTTPRequest(url): #non-real time
    resp = urllib.request.urlopen(url)
    print(resp.read())

    return None

def makeHTTPconnection(url): #realtime connection
    con = http.client.HTTPSConnection(url)
    con.request("GET","/")
    res = con.getresponse()
    print(res.status, " ", res.reason)
    print(res.read(1000))

    #while not res.closed:
    #   print(res.read(200))

#a URL: scheme://netloc/path;parameters?query#fragment

#line='Jan 27 00:18:58 hannah kernel: [261288.911114]  exe="/usr/bin/dbus-daemon" sauid=103 hostname=? addr=? terminal=?'
#line : [date] [time] [hostname] [process] [message]
def parsing ():
    #identify the format of the lines
    # date
    sample = 'Jan 27 00:18:58 hannah kernel: [261288.911429]  exe="/usr/bin/dbus-daemon" sauid=103 hostname=? addr=? terminal=?'
    test = 'vin9 tran'

    line = 'Jan 27 00:18:58 hannah kernel: [261288.911114]  exe="/usr/bin/dbus-daemon" sauid=103 hostname=? addr=? terminal=?'
    #step 1: identify the sub patterns to form the master for one line
    date = r"(?P<date>\w+\s\w+)"
    print(date)
    time = r"(?P<time>\d+:\d+:\d+)"
    hostname = r"(?P<hostname>\w+)"
    process = r"(?P<process>\w+)"
    message = r"(?P<message>[\w\W]*)" #all the remaining of line
    spaces = r"\s*"
    masterPattern = spaces.join([date,time,hostname,process,message])
    #do not use join(), unless '|'.join() or '&'.join() because it returns not re pattern
    #masterPattern = date+spaces+time+spaces+hostname+spaces+process+spaces+message
    #masterPattern = date+spaces+time+spaces+hostname+spaces+process+spaces+message

    print(masterPattern)
    # scanner = re.match(masterPattern, line)
    # print(scanner)
    scanner = re.compile(masterPattern)
    ob = scanner.match(line)
    print(ob.groups())
    print(ob.groupdict())
    copyDict = dict(ob.groupdict())

    answer = {}
    with open("sample.log", "r") as f:
        index = 0
        for line in f:
            ob = scanner.match(line)
            #print(ob.groupdict())
            answer[index] = dict(ob.groupdict())
            index += 1

    for key in answer.items():
        print(key)

    values = answer.values()
    query = sorted(answer.values(), key= lambda k: k['process'])

    # mess = 'message'
    # print(answer[2][mess])
    for i in query:
        print(i['process'], " ", i['date'], " ", i['time'], i['message'])
    # for i in values:
    #     print(i)

    #if you have a matrix, so how to sort it by each keys fast in python

    return None




if __name__ == '__main__':
    #makeSampleHTTPRequest("https://docs.python.org")
    #makeHTTPconnection("docs.python.org")
    parsing()



''' Puzzles
You need to distribute a terabyte of data from a single server to 10,000 nodes, 
and then keep that data up to date. 
It takes several hours to copy the data just to one server. 
How would you do this so that it didn't take 20,000 hours 
to update all the servers? Also, how would you make sure that the file wasn't 
corrupted during the copy? 

First was a fizz buzz type question. Second and third were both log parsing. Last one was involved in Linkedin RESTful api calling and recursion. 
Print all statistics of every process name and its log for every minute of a piece of system log.    
Recursive call of LinkedIn api using REST.
Explain ssh connection
The coding round is easy. 5 questions. One had to be done by recursion, others were on text processing. It was on coderpad.io. You can use any language you want to code.
2 conceptual/design interviews. Many questions on systems knowledge ( networks, OS, linux, ssl, etc). To prepare: read the networks: top down approach book. For linux, do unix and linux sys admins handbook. 
For system design, google "system design primer". Its a github link.
How HTTPS works  
'''