#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#먼저 함수2를 호출하는데 num에 2를 대입하고 그 결과 num은 12가 된다. 그리고 return으로 인해 함수1을 호출해 num에 12를 대입하면 num은 12+2=14 가 된다. 마지막으로 다시 한번 return으로 함수0을 호출해 14*2=28이 된다.
#답: 28

