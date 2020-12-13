#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
#만약 과일이 values안에 있다면 정답입니다. 가 출력되고, 없다면 오답입니다. 가 출력된다.

