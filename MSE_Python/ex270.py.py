#!/usr/bin/env python
# coding: utf-8

# In[15]:


class stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

종목 = []

삼성 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
#함수를 만들고 종목에 삼성, 현대차, LG전자의 항목을 리스트로 추가해 for 문을 이용하여 함수에 해당하는 code, per 부분을 도출한다.
#답: 005930 15.79
#  005380 8.7
#  066570 317.34

