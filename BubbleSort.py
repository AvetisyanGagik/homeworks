#Bubble sort

mylist = [4,8,15,95,25,1,0,874,54,96,56,0]

for j in range(len(mylist)):
    for i in range(len(mylist)-1):
        if mylist[i]>mylist[i+1]:
            mylist[i], mylist[i+1] = mylist[i+1] , mylist[i]
print(mylist)
