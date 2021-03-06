'''
Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn" instead.

'''

# if __name__=='__main__':
#     l,n = "Linked", "In"
#     for i in range(1,101):
#         message =  (l+n if i%6 == 0 else l ) if i%4 == 0 else ( n if i%6==0 else str(i))
#         print(message)


'''
Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information. The employee information endpoint is "/employee/<id>". Each employee record you retrieve will be a JSON object with the following keys:

  - 'name'  refers to a String that contains the employee's first and last name

  - 'title' refers to a String that contains the employee's job title

  - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports

Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.

For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.


-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Software Engineer
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
'''

'''
import urllib.request
import urllib.parse

def makeQuery(employeeID):
    link = "http://www.linkedin.corp/api"
    values = {'q': employeeID }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') #assume API using UTF-8
    #build a request obj
    req  = urllib.request.Request(link,data, method='POST')
    answer = ''
    with urllib.request.urlopen(req) as resp:
        answer = resp.read()

    #parsing the answer (Jason obj to dictionary = {'name': value, 'title' : value, 'reports': value}
    pass

    #return that answer as dictionary

    return answer



if __name__ == '__main__':
    #read input
    employeeID = input()

    #

    #make a query to get the employeeID 's info
    answer = makeQuery(employeeID)
    if answer != '':
        pass
    else:
        print("Error: ", employeeID, " not found")

    #build the tree using the DFS 
    root = employeeID
    visited = {}

    while 

    #parsing 

'''

'''
Below, see a sample of /var/log/messages.

---------- begin sample log extract ----------
Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
Jan 20 03:25:09 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
Jan 20 03:26:22 fakehost anacron[28969]: Normal exit (1 job run)
Jan 20 03:30:01 fakehost CROND[31462]: (root) CMD (/usr/lib64/sa/sa1 1 1)
Jan 20 03:30:01 fakehost CROND[31461]: (root) CMD (/var/system/bin/sys-cmd -F > /dev/null 2>&1)
Jan 20 05:03:03 fakehost ntpd[3705]: synchronized to time.faux.biz, stratum 2
Jan 20 05:20:01 fakehost rsyslogd: [origin software="rsyslogd" swVersion="5.8.10" x-pid="20438" x-info="http://www.rsyslog.com"] start
Jan 20 05:22:04 fakehost cs3[31163]:  Q: ".../bin/rsync -LD ": symlink has no referent: "/var/syscmds/fakehost/runit_scripts/etc/runit/service/superImportantService/run"#012Q: ".../bin/rsync -LD ": rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1039) [sender=3.0.6]
Jan 20 05:22:04 fakehost cs3[31163]:  I: Last 2 quoted lines were generated by "/usr/local/bin/rsync -LD --recursive --delete --password-file=/var/syscmds/modules/rsync_password /var/syscmds/fakehost syscmds@fakehost::syscmds_rsync"
Jan 20 05:22:08 fakehost cs3[31163]:  Q: ".../sbin/sv restart": ok: run: /export/service/cool-service: (pid 32323) 0s
Jan 20 05:22:08 fakehost cs3[31163]:  I: Last 1 quoted lines were generated by "/sbin/sv restart /export/service/cool-service"
Jan 20 05:22:09 fakehost cs3[31163]:  R: cs3:  The cool service on fakehost does not appear to be communicating with the cool service leader.  Automating a restart of the cool service in attempt to resolve the communication problem.
Jan 20 05:22:37 fakehost ACCT_ADD: WARNING: Manifest /var/syscmds/inputs/config-general/doit.txt has been processed already, bailing
---------- end sample log extract ----------


Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages in sorted time order.


---------- begin sample output ----------
minute, number_of_messages
Jan 20 03:25,2
Jan 20 03:26,2
Jan 20 03:30,2
Jan 20 05:03,1
Jan 20 05:20,1
Jan 20 05:22,6
---------- end sample output ------------ 
'''

with open(fileName, "r") as f :
    for line in f:
        s = line.split(' ', 3)
        date = s[0] + ' ' +  s[1] + ' '
import re

def parsing():
    fileName = '/var/log/message'


# build the scanner
date = r"(?P<date>\w+\s+\w+)"
time = r"(?P<time>\d+:\d+:\d+)
message = r"(?P<message>[\w\W]*)"  # the remaining
spaces = r"\s*"
masterPattern = spaces.join([date, time, message])
scanner = re.compile(masterPattern)
answers = {}
with open(fileName, 'rt') as fin:
    index = 0
    for line in fin:
        result = scanner.match(line).groupdict()
        answers[index] = [result['date'], result['time']]

final = sorted(answers.values(), key=lambda k: k['time'])

count = 0
n = len(final.keys()
        for i in range(n):
if i - 1 >= 0:
    if
final[i] == final[i - 1]:
count += 1
else:
done = True
if done:
    print(final[i][0], " ", final[i][1], ",", count)

return None



