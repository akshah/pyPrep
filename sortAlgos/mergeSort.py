#!/usr/bin/python
def merge(leftA, rightA):
    results=[]
    li=0
    ri=0
    while li<len(leftA) and ri<len(rightA):
        if leftA[li]<rightA[ri]:
            results.append(leftA[li])
            li+=1
        else:
            results.append(rightA[ri])
            ri += 1
    while li<len(leftA):
        results.append(leftA[li])
        li+=1
    while ri<len(rightA):
        results.append(rightA[ri])
        ri+=1
    return results

def mergeSort(array):
    if len(array)<2:
        return array
    mid=len(array)//2
    leftArray=mergeSort(array[:mid])
    rightArray=mergeSort(array[mid:])
    results=merge(leftArray,rightArray)

    return results


if __name__=="__main__":
    arr=[1,3,5,2,5,6,2,3,4,5,6]
    print(arr)
    sortedArr=mergeSort(arr)
    print(sortedArr)

    

