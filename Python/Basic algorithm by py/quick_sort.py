#py3实现快速排序，三个版本


#标准算法，严蔚敏书中的伪代码实现

"""
def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low

if __name__ == '__main__':
    array2 = [9,3,2,1,4,6,7,0,5]

    print(array2)
    quick_sort_standord(array2,0,len(array2)-1)
    print(array2)

"""

"""
#这是特殊实现
#!/usr/bin/python
# -*- coding: utf-8 -*-


def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort1(array,low,high):
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort1(array,low,key_index)
        quick_sort1(array,key_index+1,high)

if __name__ == '__main__':
    #array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    array1 = [7,3,5,6,2,4,1]

    print(array1)
    quick_sort1(array1,0,len(array1)-1)
    print(array1)

"""

#三行实现快速排序

#coding:utf-8
def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+ \
    qsort([ge for ge in L[1:] if ge >= L[0]])

iList = [3,14,2,12,9,33,99,35]

print(iList)
print(qsort(iList))
