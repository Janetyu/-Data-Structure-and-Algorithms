"""
负载因子
你的一名同事拿着一个散列函数来找你，这个函数用一组除以100，使用余数作为关键字。
这些值为100个数字，且都是5的倍数，那么负载因子是多少？
100/100=1,负载因子为1

他认为这个速度有点慢，那你建议函数除以多少（而非100）来加快查找速度呢？

a.87，比125好，但它比100小，所以依然会有冲突
b.107，相比之下，107是最好的
c.125，它是5的倍数，但其他5的倍数除以125取余后，结果是5和0，会产生很多冲突
d.1001，它是可行的，但是它会产生很多剩下的哈希桶，浪费空间

选b，
"""
