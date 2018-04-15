"""
py实现递归算法

function recursive(input):
    if input <= 0:
        return input
    else
        output = recursive(input - 1)
        return output
"""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position-1) + get_fib(position - 2)

#Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))

