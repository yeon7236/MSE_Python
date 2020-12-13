#!/usr/bin/env python
# coding: utf-8

# In[2]:


def message1():
    print("A")
    
def message2():
    print("B")
    
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
    
message3()
#for문에서 3번 반복해서 message2()와 C를 출력하고 message1()을 출력한다.
#답:B C B C B C A

