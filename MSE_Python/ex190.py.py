#!/usr/bin/env python
# coding: utf-8

# In[1]:


apart = [ [101, 102], [201,202], [301,302] ]

for row in apart:
    for col in row:
        print(col, "호")
print("-" * 5)
#apart안에 있는 리스트 각각에 '호'를 붙이는 for문을 만들어서 출력하고 마지막에 -----를 출력했다.
#답: 101 호
#   102 호
#   201 호
#   202 호
#   301 호
#   302 호
#   -----

