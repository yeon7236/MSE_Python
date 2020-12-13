#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(변수)
#split를 이용해 .을 기준으로 나누고 h나 c가 있다면 그것을 출력하게 된다.
#답: intra.h intra.c define.h

