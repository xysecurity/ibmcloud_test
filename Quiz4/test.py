# count=[[1,5,0],[5,10,0],[10,20,0],[20,50,0],[50,100,0]]
# if 65>count[4][0] and 90<count[4][1]:
# 	count[4][2]+=1

# print(range(len(count)))
# for i in range(len(count)):
# 	print (count[i])
# print(65>count[4][0] and 110<count[4][1])
import random
import sqlite3
import redis
# r=redis.Redis(host='anakin.redis.cache.windows.net',port=6379,password='QuhFzLTrVd+LNdWaF1fAxikpgc6bdfiaimiqk2PJB44=',decode_responses=True)
# a=round(random.uniform(0,9),1)
# print(a)
# print(float(2095)/3717*100)
number='1234'
print(number[-1])
def cal(number):
	a=number*number*number
	str1=''
	str1=str(a)
	int1=0
	int1=int(str1[-1])
	return int1
print(cal(3))




