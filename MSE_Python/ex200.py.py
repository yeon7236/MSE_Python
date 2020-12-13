#!/usr/bin/env python
# coding: utf-8

# In[2]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
#for문을 이용해 닫힐 때의 금액에서 열릴 때의 금액을 빼는 것을 반복하면 3일 간의 수익금을 계산할 수 있다.
#답: 1일차 수익 0원. 2일차 수익 -10원, 3일차 수익 10원

