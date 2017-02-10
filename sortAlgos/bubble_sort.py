def bubble_sort(alist):
    passnum = len(alist) - 1
    while passnum > 0:
        for j in range(passnum):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
        passnum -= 1

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)
