
a=[(1,2), (3,4), (9,8)]
n = len(a)
# for i in range(n):
#     print(i)
#     del a[i]
#     print(a)

for i,v in enumerate(a):
    print(a)
    a.pop(i)

print(a)