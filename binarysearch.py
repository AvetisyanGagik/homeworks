some_list = [1,5,8,10,65,555]
search = int(input('enter a number'))
start = 0
end = len(some_list)-1
while True:
    mid = (start + end) // 2
    if search == some_list[mid]:
        print(mid)
        break
    else:
        if search > some_list[mid]:
            start = mid+1
        else:
            end = mid-1



