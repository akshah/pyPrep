#/usr/bin/python
def binary_search_iterative(arr,left,right,valToCompare):
    while left<=right:
        mid=(left+right+1)//2
        if valToCompare==arr[mid]:
            return mid
        elif valToCompare>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return "Not found"

def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binary_search(alist[:midpoint],item)
            else:
                return binary_search(alist[midpoint+1:],item)

if __name__=="__main__":
    array=[1,2,3,4,5,6,7]
    print(binary_search(array,7))
    print(binary_search_iterative(array,0,len(array)-1,1))
