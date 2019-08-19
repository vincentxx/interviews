#plays with subprocess
import subprocess

fileName = "/home/vuqt1/interviews/output"
def playSubprocess():
    with open(fileName, "w") as f:
        # subprocess.run(["ls", "-tral"], stdout=f)
        # subprocess.run(["cat", fileName])

        #cat fileName | grep search

        #subprocess.run(["cat", fileName], stdout=)
        text = b'./output'
        p = subprocess.Popen(["grep", "a"], stdin= subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        output = p.communicate("/home/vuqt1/interviews/output")


        #dmesg | grep hda
        # p1 = subprocess.Popen(["dmesg"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # p2 = subprocess.Popen(["grep", "hda"], stdin=p1.stdout, stdout= subprocess.PIPE)
        # output = p2.communicate()[0]
        print(output)

playSubprocess()

##converntional

"""
os.fork()
os.pipe()
os.write()
os.open()

"""