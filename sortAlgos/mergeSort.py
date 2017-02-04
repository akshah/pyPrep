#!/usr/bin/python

def merge_sort(array):
    mid=len(array)//2
    leftArray=merge_sort(array[:mid])
    rightArray=merge_sort(array[mid:])

    

