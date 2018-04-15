#冒泡排序练习
"""
如果对[21,4,1,3,9,20,25,6,21,14]进行冒泡排序，第三次迭代会是怎样的？

答案是: [4,1,3,9,20,21,6,21,14,25]  (1)
        [1,3,4,9,20,6,21,14,21,25]  (2)
        [1,3,4,9,6,20,14,21,21,25]  (3)
        [1,3,4,6,9,14,20,21,21,25]  (4)
"""


#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
简介:本程序主要是用python实现冒泡排序，程序的功能是实现
     降序排列。
'''

class BubbleSort(object):
    '''
    self.datas:       要排序的数据列表
    self.datas_len:   数据急的长度
    _sort():          排序函数
    show():           输出结果函数

    用法：
    BubbleSort(datas) 实例化一个排序对象
    BubbleSort(datas)._sort() 开始排序，由于排序直接操作
                              self.datas, 所以排序结果也
                              保存在self.datas中
    BubbleSort(datas).show()  输出结果
    '''
    def __init__(self, datas):
        self.datas = datas
        self.datas_len = len(datas)

    def _sort(self):
        #冒泡排序要排序n个数，由于每遍历一趟只排好一个数字，
        #则需要遍历n-1趟，所以最外层循环是要循环n-1次，而
        #每次趟遍历中需要比较每归位的数字，则要在n-1次比较
        #中减去已排好的i位数字，则第二层循环要遍历是n-1-i次
        for i in range(self.datas_len-1):
            for j in range(self.datas_len-1-i):
                if(self.datas[j] < self.datas[j + 1]):
                    self.datas[j], self.datas[j+1] = \
                            self.datas[j+1], self.datas[j]

    #升序排序
    def asc_sort(self):
        for i in range(self.datas_len - 1):
            #减去i是为了减去不需要重复判断的部分
            for j in range(self.datas_len - 1 - i):
                if(self.datas[j] > self.datas[j + 1]):
                    self.datas[j],self.datas[j+1] = \
                            self.datas[j+1],self.datas[j]

    def show(self):
        print('Result is:')
        for i in self.datas:
            print(i)
        print('')

if __name__ == '__main__':
    try:
        datas = input('Please input some number:')
        datas = datas.split()
        datas = [int(datas[i]) for i in range(len(datas))]
    except Exception:
        pass

    bls = BubbleSort(datas)
    print("降序冒泡排序：")
    bls._sort()
    bls.show()
    print("升序冒泡排序：")
    bls.asc_sort()
    bls.show()
