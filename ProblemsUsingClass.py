# Ticket numbers usually consist of an even number of digits.A ticket number is
# considered lucky if the sum of the first half of the digits is equal to the sum of the
# second half.Given a ticket number n, determine if it's lucky or not. Example For
# n = 1230, the output should be
# Lucky(n) = true;
# For n = 239017,
# the output should be Lucky(n) = false





# class Luck:
#     def __init__(self,number,list1,list2):
#         self.number = number
#         self.list1 =list1
#         self.list2 = list2
#     def func(self):
#         for i, j in zip(self.number[:len(self.number)//2+1],self.number[len(self.number)//2:]):
#             self.list1.append(int(i)), self.list2.append(int(j))
#         return sum(self.list1) == sum(self.list2)
# x = Luck('12000344',[],[])
# print(x.func())

#_-----------------------------------------------------------------------------------------------


# Several people are standing in a row and need to be divided into two teams. The
# first person goes into team 1, the second goes into team 2, the third goes into
# team 1 again, the fourth into team 2, and so on.You are given an array of positive
# integers - the weights of the people. Return an array of two integers, where the
# first element is the total weight of team 1, and the second element is the total
# weight of team 2 after the division is complete.
# Example For a = [50, 60, 60, 45, 70], the output should be
# alternating Sums(a) = [180, 105].



# class Weight:
#     def __init__(self,mainlst,lst1,lst2):
#         self.mainlst = mainlst
#         self.lst1 = lst1
#         self.lst2 = lst2
#     def main(self):
#         for i in range(0,len(self.mainlst),2):
#             self.lst1.append(self.mainlst[i])
#             # self.lst2.append(self.mainlst[i+1])
#         for j in range(1,len(self.mainlst),2):
#             self.lst2.append(self.mainlst[j])
#         return [sum(self.lst1),sum(self.lst2)]

# final = Weight([50, 60, 60, 45, 70],[],[])
# print(final.main())

#__________________________________________________________________________________________________________________

# Create a class: Some people are standing in a row in a park. There are trees
# between them which cannot be moved. Your task is to rearrange the people by
# their heights in a non-descending order without moving the trees. People can be
# very tall!
# Example
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

# class Sorting:
#     def __init__(self,mainlist):
#         self.mainlist = mainlist
#     def func(self):
#         indexes_list = list()
#         for i in range(len(self.mainlist)):
#             if self.mainlist[i] == -1:
#                 indexes_list.append(i)
#         for k in range(len(indexes_list)):
#             self.mainlist.remove(-1)
#         self.mainlist.sort()
#         for i in range(len(indexes_list)):
#             self.mainlist.insert(indexes_list[i],-1)
#         return self.mainlist
# x = Sorting([-1, 600, 190, 170, -1, -1, 160, 180,-1,-1,500])
# print(x.func())
#
#
#
# x = Sorting([-1, 150, 190, 170, -1, -1, 160, 180])


# Create a class which given a year, return the
# century it is in. The first century spans from the
# year 1 up to and including the year 100, the
# second - from the year 101 up to and including the
# year 200, etc.
# For year = 1900, the output should be = 19

# class Centuary:
#     def returnCentuary(self,year):
#         return (year+99)//100
#
# x = Centuary()
# print(x.returnCentuary(1))


# Create a class given the string, check if it is a palindrome.
# word should be lowercase and 1 ≤ inputString.length ≤ 105
# Example
# For inputString = "aabaa", the output should be true;
# For inputString = "abac", the output should be false;
# For inputString = "a", the output should be true.

# class Palindrome:
#     def palindromeOrNot(self,somestring):
#         if 1<=len(somestring)<105:
#             somestring = somestring.lower()
#             if somestring == somestring[::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             print("Run again a programm and give a number between 1 and 105 Please!!!!!!")
# x = Palindrome()
# print(x.palindromeOrNot('a'))
#






#Create a Class which given an list of integers, find the pair
# of adjacent elements that has the largest product and
# return that product.
# For inputList = [3, 6, -2, -5, 7, 3],
# the output should be = 21.


# class FindOutput:
#     def __init__(self,lst):
#         self.lst = lst
#
#     def showoutput(self):
#         for i in range(1,len(self.lst)-1):
#             outp = self.lst[0]*self.lst[1]
#             if outp< self.lst[i]*self.lst[i+1]:
#                 outp = self.lst[i]*self.lst[i+1]
#         return outp
#
#
#
# x = FindOutput([3, 6, -2, -5, 7, 3])
# print(x.showoutput())




# Create a class which given a list of strings, return another list
# containing all of its longest strings.
# Example
# For inputList = ["aba", "aa", "ad", "vcd", "aba"],
# the output should be
# allLongestStrings(inputList) = ["aba", "vcd", "aba"].



class LongestString:
    def longstr(self,lst):
        somelist = list()
        maxlen = len(lst[0])
        for i in range(1,len(lst)-1):
            if maxlen<len(lst[i]):
                maxlen = len(lst[i])
        for j in lst:
            if len(j) == maxlen:
                somelist.append(j)
        return somelist

x =LongestString()
print(x.longstr(["aba", "aa", "ad", "vcd", "aba"]))







