#!/usr/bin/env python
# coding: utf-8

# In[1]:


#try: 실행코드
#except: 예외가 발생했을 때 수행할 코드
#else: 예외가 발생하지 않았을 때 수행할 코드
#finally: 예외 발생 여부와 상관없이 항상 수행할 코드

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
# 먼저 10.31을 try하고 예외가 없기때문에 else가 실행되고 진행을 끝마치므로 finally가 실행된다. 그리고 두 번째 ""을 실행할 때는 예외가 발생 했으므로 except가 실행되고 finally가 실행된다.
# 그리고 세 번째 "8.00"을 실행할 때는 첫 번째와 마찬가지로 실행된다.
#답: 10.31  
#   clean data  
#   변환 완료  
#   0  
#   변환 완료  
#   8.0  
#   clean data  
#   변환 완료

