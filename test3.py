# -*- coding: UTF-8 -*-
import random
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
print(u"抽取一等奖1个:")
r1 = random.choice(aList)
aList.remove(r1)
print(u"一等奖是"+r1)

r2 = random.choice(aList)
aList.remove(r2)
print (u"二等奖是"+r2)

r3 = random.choice(aList)
print (u"三等奖是"+r3)