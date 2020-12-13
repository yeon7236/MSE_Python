#!/usr/bin/env python
# coding: utf-8

# In[4]:


low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [ ]
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
    
print(volatility)
#변수의 범위를 low_prices로 정해서 high에서 low를 반복적으로 뺄 수 있게 for문을 이용한다.
#답:[50, 100, 30, 80, 0]

