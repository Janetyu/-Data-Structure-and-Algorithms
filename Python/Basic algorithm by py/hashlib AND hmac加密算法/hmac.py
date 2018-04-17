"""
hashmac模块简介：

前面说过，HMAC算法也是一种一种单项加密算法，
并且它是基于上面各种哈希算法/散列算法的，
只是它可以在运算过程中使用一个密钥来增增强安全性。
hmac模块实现了HAMC算法，提供了相应的函数和方法，
且与hashlib提供的api基本一致。


hmac模块使用步骤：

hmac模块模块的使用步骤与hashlib模块的使用步骤基本一致，
只是在第1步获取hmac对象时，只能使用hmac.new()函数，
因为hmac模块没有提供与具体哈希算法对应的函数来获取hmac对象。


"""
#!/usr/bin/env python
# coding=utf-8
__author__ = 'Luzhuo'
__date__ = '2017/5/19'
# hmac_demo.py HMAC算法
# 与hashlib不同之处在于多了key
 
import hmac
 
 
def hmac_demo():
  # 加密
  h = hmac.new(b"net")
  h.update(b"luzhuo.me")
  h_str = h.hexdigest()
  print(h_str)
 
  # 比较密码
  boolean = hmac.compare_digest(h_str, hmac.new(b"net", b"luzhuo.me").hexdigest())
  print(boolean)
 
  
 
def hmac_func():
  # 创建key和内容,再都进行加密
  # hmac.new(key, msg=None, digestmod=None) // 创建新的hmac对象, key:键, msg:update(msg), digestmod:hash名称(同hashlib.new())(默认md5)
  hc = hmac.new(b"key")
 
  # hmac对象
  hc.update(b"msg") # 字节缓冲区 hc.update(a) hc.update(b) == hc.update(a+b)
  hash_bytes = hc.digest() # 字节hash
  hash_str = hc.hexdigest() # 16进制hash字符串
  hc = hc.copy() # 拷贝hmac副本
  num = hc.digest_size # hash大小
  num = hc.block_size # hash算法内部块大小
  strs = hc.name # hash名称
  # hmac.compare_digest(a, b) // 比较两个hash密钥是否相同, 参数可为: str / bytes-like object, (注:建议使用,不建议使用a==b)
  boolean = hmac.compare_digest(hmac.new(b"net", b"luzhuo.me").digest(), hmac.new(b"net", b"luzhuo.me").digest())
 
  
 
 
if __name__ == "__main__":
  hmac_demo()
 
  # hmac_func()
