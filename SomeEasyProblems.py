# Firts------------->>>>>>>>>>.
# start = int(input())
# stop = int(input())
# step = int(input())
# def createlist(start,stop,step):
#     return [i for i in range(start,stop,step)]#Second
# mylist = [3,7,12,5,20,0]
# newlist = []
# def hello(mylist):
#     for i in range(len(mylist)-1):
#         newlist.append(mylist[i]*mylist[i+1])
#     return newlist
# print(hello(mylist))#for
# some_list = ['anymore', 'raven', 'me', 'communicate']
# def lenlist(some_list):
#     new_list = []
#     for i in some_list:
#         new_list.append(len(i))
#     return min(new_list)+ max(new_list)
# print(lenlist(some_list))#Five
# n = int(input('enter a number'))
# lst = []
# somelist = [36, -12, 47, -58, 148, -55, -19, 10]
# for i in range(len(somelist)):
#     if n in somelist:
#         print(somelist.index(n))
#         break
#     else:
#         minimum = 0
#         for j in range(len(somelist)):
#             if abs(somelist[j]-n)<abs(somelist[minimum]-n):
#                 minimum = j
#                 lst.append(minimum)
#         print(lst[-1])
#         break#Six
# n = int(input('enter a number'))
# mydict = dict()
# for i in range(n+1):
#     mydict[i] = i**2
# print(mydict)
#
# #7
# Given an dict. Invert it (keys become values and values

# become keys). If there is more than key for that given value

# create an list.Input

# { a: ‘1’, b: ‘2’, c: ‘2’ }

# Output

# { 1: ‘a’, 2: [‘b’, ‘c’] }


def invert():
    smdict = dict()
    mydict = {'a':1,'b':2,'c':2,'d':2,'f':1}
    keys = list(mydict.keys())
    # print(keys)
    vals = list(mydict.values())
    for i , j in zip(keys,vals):
        if j not in smdict:
            smdict[j] = i
        else:
            x = list(smdict.get(j))
            x.append(i)
            smdict[j] = x
    print(smdict)

invert()