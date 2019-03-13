def binarySearch (x,arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        print(i, " ", j)
        m = int((i+j)/2)
        if x > arr[m]:
            i = m + 1
        else:
             j = m

    if x == a[i]:
        return i
    else:
        return "Not found"

    pass


def heapSort(arr):
    buildHeap(arr)

    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, school):
        self.school = school
        Person.name = name
        Person.age = age


class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    def __init__(self, node):
        self.root = node


if __name__ == '__main__':
    # a = [1,3,4,6,7,9,11]
    # m = binarySearch(6,a)
    # print("the index found is: ", m)

    person = Person("John", 19)
    #John = Student("John")
    john = Student("John", 18, "UCI")
    print(john.name, john.age)

