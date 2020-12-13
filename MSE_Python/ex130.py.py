#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#만약 시가와 변동폭의 합이 최고가 보다 크다면 상승장을 출력하고, 합이 더 작다면 하락장을 출력한다.
#답: 상승장

