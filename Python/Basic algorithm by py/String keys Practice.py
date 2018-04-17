#字符串键练习  hash表练习

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self,string):
        """输入一个字符串然后存在这个表中"""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]
        
    def lookup(self,string):
        """返回一个hash值，当这个字符已经存在这个表中，否则返回-1"""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    print(self.table[hv])
                    return hv
        return -1

    def calculate_hash_value(self,string):
        """计算字符串的哈希值"""
        value = ord(string[0])*100 + ord(string[1])
        return value


#开始
hash_table = HashTable()

#测试计算哈希值
#should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

#测试查找
#should be -1
print(hash_table.lookup('UDACITY'))

#测试存储
hash_table.store('UDACITY')
#should be 8568
print(hash_table.lookup('UDACITY'))

#测试存储另外一个字符串
hash_table.store('UDACIOUS')
#should be 8568
print(hash_table.lookup('UDACIOUS'))


