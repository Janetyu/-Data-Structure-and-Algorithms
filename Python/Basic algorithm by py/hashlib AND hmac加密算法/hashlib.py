"""
不可逆加密

hashlib模块简介：

hashlib模块为不同的安全哈希/安全散列（Secure Hash Algorithm）和 信息摘要算法（Message Digest Algorithm）
实现了一个公共的、通用的接口，也可以说是一个统一的入口。
因为hashlib模块不仅仅是整合了md5和sha模块的功能，
还提供了对更多中算法的函数实现，
如：MD5，SHA1，SHA224，SHA256，SHA384和SHA512。

hashlib模块使用步骤：

1）获取一个哈希算法对应的哈希对象（比如名称为hash）：
可以通过 hashlib.new(哈希算法名称, 初始出入信息)函数，来获取这个哈希对象，
如hashlib.new('MD5', 'Hello')，hashlib.new('SHA1', 'Hello')等；
也可以通过hashlib.哈希算法名称()来获取这个哈希对象，
如hashlib.md5(), hashlib.sha1()等。

2）设置/追加输入信息：
调用已得到哈希对象的update(输入信息)方法可以设置或追加输入信息，
多次调用该方法，等价于把每次传递的参数凭借后进行作为一个参数垫底给update()方法。
也就是说，多次调用是累加，而不是覆盖。

3）获取输入信息对应的摘要：
调用已得到的哈希对象的digest()方法或hexdigest()方法即可得到传递给update()方法的字符串参数的摘要信息。
digest()方法返回的摘要信息是一个二进制格式的字符串，
其中可能包含非ASCII字符，包括NUL字节，该字符串长度可以通过哈希对象的digest_size属性获取；
而hexdigest()方法返回的摘要信息是一个16进制格式的字符串，
该字符串中只包含16进制的数字，且长度是digest()返回结果长度的2倍，
这可用邮件的安全交互或其它非二进制的环境中。


"""
#!/usr/bin/env python
# coding=utf-8
__author__ = 'Luzhuo'
__date__ = '2017/5/19'
# hash_demo.py Hash加密相关(安全哈希)
# 支持: MD5, SHA1 SHA224 SHA256 SHA384 SHA512
 
 
import hashlib
 
 
def hash_demo():
  m = hashlib.md5()
  m.update(b"hello")
  m.update(b"world!") # = hello + world!
 
  hash_hex = hashlib.sha3_512(b"luzhuo.me").hexdigest()
 
  print(m.digest_size)
  print(m.digest()) # 二进制hash
  print(m.hexdigest()) # 十六进制hash
  print(hash_hex)
 
  # 加盐加密
  hash_bytes = hashlib.pbkdf2_hmac('sha256', b'luzhuo.me', b'80', 100000)
  print(hash_bytes)
 
  
 
def hash_func():
  # hashlib.new(name[, data]) // 创建hashlib(非首选), name=算法名, data:数据
  hash = hashlib.new('ripemd160', b'luzhuo.me')
 
  # 常量
  dics = hashlib.algorithms_guaranteed # 所有平台支持的hash算法的名称
  dics = hashlib.algorithms_available # 在Python解析器中可用的hash算法的名称, 传递给new()时, 可识别
 
  # hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) // 加盐加密 hash_name:hash名称, password:数据, salt:盐, iterations:循环次数, dklen:密钥长度
  hash_bytes = hashlib.pbkdf2_hmac('sha256', b'luzhuo.me', b'80', 100000)
 
  # hash对象
  num = hash.digest_size # hash结果的大小
  num = hash.block_size # hash算法的内部块的大小
  strs = hash.name # hash名称, 可传给new()使用
  hash.update(b"data") # 字节缓冲区 hash.update(a) hash.update(b) == hash.update(a+b)
  hash_bytes = hash.digest() # 字节hash
  hash_str = hash.hexdigest() # 16进制字符串hash
  hash = hash.copy() # 拷贝hash对象副本
 
  
 
if __name__ == "__main__":
  hash_demo()
 
  # hash_func()
