"""
py实现二分查找算法
"""

def binary_search1(input_array,value):
    #非递归
    n = len(input_array)
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if value == input_array[mid]:
            return True
        elif value < input_array[mid]:
            end = mid - 1
        elif value > input_array[mid]:
            start = mid + 1
            
    return False

def binary_search2(input_array,value):
    #递归
    n = len(input_array)
    if 0 == n:
        return False
    mid = n // 2
    if value == input_array[mid]:
        return True
    elif value < input_array[mid]:
        return binary_search2(input_array[:mid],value)
    elif value > input_array[mid]:
        return binary_search2(input_array[mid+1:],value)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print("binary_search1:"+ str(binary_search1(test_list,test_val1)))
print("binary_search2:"+ str(binary_search2(test_list,test_val1)))
print("binary_search1:"+ str(binary_search1(test_list,test_val2)))
print("binary_search2:"+ str(binary_search2(test_list,test_val2)))
