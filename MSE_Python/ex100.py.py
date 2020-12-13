#!/usr/bin/env python
# coding: utf-8

# In[2]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
#zip으로 date와 close_price를 연결해주면 순서대로 묶이게 된다. 그리고 이것을 dict하면 중괄호로 표현된다.
#답:{09/05 10500} {09/06 10300} {09/07 10100} {09/08 10800} {09/09 11000}
