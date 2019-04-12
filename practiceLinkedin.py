#!/usr/bin/env python3
##Site Reliability Engineer - Entry level
##http request, filesystem processing, algorithm + data structure
import urllib.request
import urllib.parse
import http.client
import html.parser
#from html.parser import HTMLParser
import re

'''
Note that urlopen returns a bytes object. This is because there is no way for urlopen to 
automatically determine the encoding of the byte stream it receives from the HTTP server. 
In general, a program will decode the returned bytes object to string once it determines 
or guesses the appropriate encoding.
https://docs.python.org/3.6/library/urllib.parse.html#module-urllib.parse
https://docs.python.org/3.6/library/urllib.request.html#urllib-examples
#https://docs.python.org/3.6/howto/urllib2.html#urllib-howto
'''
def makeSampleHTTPRequest(url): #non-real time
    #resp = urllib.request.urlopen(url)
    #print(resp.read())

    #practice with parsing an URL
    link = "https://docs.python.org/3.6/library/urllib.parse.html#module-urllib.parse"
    urlTuple = urllib.parse.urlparse(link)
    #print(urlTuple)

    #make a POST request to search for "vincent"
    link= "https://pythonprogramming.net/search"
    #build the values of the data: this case the query value
    #urllib.parse.urlencode will get an dict of key/values or sequence of tuple-2 (k,v)
    #  as input to encode it to url format
    #The resulting string is a series of key=value pairs separated by '&' characters,
    # where both key and value are quoted using the quote_via function
    #then convert url format to byte or the type of server encode accepted
    values = {'q': 'robot'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') #bytes now, depending on server's accepting encode
    #make a Request obj
    req = urllib.request.Request(link,data,method='POST')
    with urllib.request.urlopen(req) as resp: #get response obj, catching exception
        parser = MyHTMLParser()
        text = resp.read()
        #parser.feed('<html><head><title>Test</title></head> <body><h1>Parse me!</h1></body></html>')
        parser.feed(text.decode())
        #print(pars)
        #print(resp.read())

    return None

#need to study basic Python classes & inheritance
class MyHTMLParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            print("start tag: ", tag)

    def handle_data(self, data):
        print(data.strip())
    def handle_endtag(self, tag):
        if tag == 'body':
            print("end tag:", tag)

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
    hostname = r"(?P<hostname>\S+)"
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

#lamda function can call other function => awesome: key= lambda k: upperKey(k['process']))
# def upperKey(s):
#     print("call upperKey")
#     return s.upper()

#Ref: https://docs.python.org/3/library/stdtypes.html#str.split
def waysGetInputs():
    n = int(input("Input the size n:"))
    line = str(input("Input the array: "))
    parseLine = list(map(int,line.split()))
    #arr = list(map(int, input().rstrip().split())) #strip off right trailing spaces

    print(parseLine)
    print(type(parseLine[1]))
    return None

# class dict(**kwarg) # **kwarg is: keyworded arguments: = dict {"arg1": value1, "arg2":val2, ..}
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
'''Return a new dictionary initialized from an optional positional argument 
and a possibly empty set of keyword arguments.
If no positional argument is given, an empty dictionary is created. 
If a positional argument is given and it is a mapping object, a dictionary is created
with the same key-value pairs as the mapping object. Otherwise, the positional 
argument must be an iterable object. Each item in the iterable must itself 
be an iterable with exactly two objects. The first object of each item becomes a key 
in the new dictionary, and the second object the corresponding value. If a key occurs more 
than once, the last value for that key becomes the corresponding value in the new dictionary'''
#https://docs.python.org/3/tutorial/datastructures.html
def waysWithDict():
    dict1 = dict(one=1, two=2, three=3)
    dict1 = dict({'one':1, 'two': 2}, three=3)
    dict1 = dict([('one',1), ('two',2)], three=3)
    dict1 = {'one':1, 'two':2, 'three': 3} #only with mappings obj
    dict1 = {k:v for k,v in [('one',1), ('two',2), ('three',3)]} # the inside return mapping obj
    #comprehension forms: {k:v for k,v in iterable}, v could be f(k)
    dict1 = {k:k*2 for k in range(3)}
    dict1 = {k:v for k,v in enumerate(range(3))}
    #using map function, map will generate a mapping obj to dict() constructor
    dict1 = dict(map(lambda x: (x,x*2), range(3))) #lamda must return iter with 2 objects
    print(dict1)

    return None

#ways withList
#https://docs.python.org/3/tutorial/datastructures.html
# [[row[i] for row in matrix] for i in range(4)] => transpose the row with column
# list(zip(*matrix)) ?? #zip(*iterables) : *iterables mean one or more iterables
#https://docs.python.org/3/library/functions.html#zip


#unresolved questions
#python generate list of variables??


#lambda: https://docs.python.org/3/reference/expressions.html#lambda
'''
lambda_expr        ::=  "lambda" [parameter_list] ":" expression
lambda_expr_nocond ::=  "lambda" [parameter_list] ":" expression_nocond
Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. 
The expression lambda parameters: expression yields a function object. 
The unnamed object behaves like a function object defined with:
def <lambda>(parameters):
    return expression
'''
import fileinput #this package has interface to get stdin or multiples files
#usage: this_script_itself < testFile1 testFile2  (also work with pipeline )
def getInput():
    with fileinput.input() as fin:
        #print(fin.filename())
        for line in fin:
            print(line)

    return None

import getpass
def getRuntimePassword():  #must test it on running script on terminal, not on pycharm for hidden pass
    user = input("Username: ")
    password = getpass.getpass(prompt="Password(hidden): ") #this module run with hidden password prompt on Unix
    print(password)
    pass #do something with username,password
    return None

import os
import shutil
import subprocess
import logging
def sampleAdminTasks():
    fileName = 'fileTest1'
    if not os.path.exists(fileName):    #check if filepath is valid
        with open(fileName, "wt") as f:
            for i in range(10):
                f.write("line " + str(i) + "\n")
    shutil.copy(fileName, 'fileTest1Copy') #using copy file by shell
    #shutil.copytree(src,dest)
    print (os.stat(fileName)) #print file statistic
    subprocess.run(['ls', '-l']) #run a command on shell
    p = subprocess.Popen(['wc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = p.communicate(b"this is vincent") #only accept byte stream
    print ("out: ", out)
    logging.basicConfig(
        filename = 'sampleAdminTask.log',
        level = logging.INFO,
        format= '%(asctime)s: %(levelname)s: %(message)s'
    )
    logging.error("this is error level")
    logging.critical("this is critical msg ")
    subprocess.run(["cat",'sampleAdminTask.log'])
    subprocess.run(['rm', '-f', 'sampleAdminTask.log'])
    return None

if __name__ == '__main__':
    #makeSampleHTTPRequest("https://docs.python.org")
    #makeHTTPconnection("docs.python.org")
    #parsing()
    #waysGetInputs()
    #waysWithDict()
    #getInput()
    #getRuntimePassword()
    sampleAdminTasks()
    pass




''' Puzzles
You need to distribute a terabyte of data from a single server to 10,000 nodes, 
and then keep that data up to date. #using the torrent ideas: point to point, spawns 2 then 2^2, 
...until all copies, write scripts number the server and do it.
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

'''
f,b="Fizz","Buzz"
for i in range(1,101):
    s=(f+b if i%5==0 else f) if i%3==0 else (b if i%5==0 else i)
    print(s)

for i in range(1,101): print (max(str(i),''+(i%3==0)*'Fizz'+(i%5==0)*'Buzz'))
'''

