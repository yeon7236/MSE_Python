#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:
    def __init__(self):
        print("부모생성")
        
class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()
        
나 = 자식()
#먼저 자식 class에 객체가 생성될 때 생성자가 호출되서 '자식생성'을 먼저 출력한다. 그 후 부모 class의 생성자를 super를 통해 명시적으로 호출했기 때문에 '부모생성'이 출력된다.
#답: 자식생성 
#   부모생성

