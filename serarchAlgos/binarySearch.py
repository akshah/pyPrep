#/usr/bin/python
def binary_search_iterative(arr,left,right,valToCompare):
    while left<right:
        mid=(left+right+1)//2
        if valToCompare==arr[mid]:
            return mid
        elif valToCompare>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return "Not found"

def binary_search(arr,left,right,valToCompare):
    if right>=1:
        mid=(left+(right+1))//2
        if valToCompare==arr[mid]:
            return mid
        elif valToCompare>arr[mid]:
            return binary_search(arr,mid+1,right,valToCompare)
        else:
            return binary_search(arr,left,mid-1,valToCompare)
    else:
        return "Not found"

if __name__=="__main__":
    array=[1,2,3,4,5,6,7]
    print(binary_search(array,0,len(array)-1,4))
    print(binary_search_iterative(array,0,len(array)-1,4))
