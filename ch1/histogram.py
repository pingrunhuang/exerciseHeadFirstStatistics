# coding:utf-8
'''
直方图用于描述定量的数据，意思是在某个数值区间内的频数
横坐标表示某个区间，纵坐标表示有多少个entry落在这个区间内
'''
import matplotlib.pyplot as plt
# from numpy.random import randn
from random import randint

x = []
frequence = [5,29,56,17,3]
for i, f in enumerate(frequence):
    x = x + [randint(i*200, (1+i)*200) for _ in range(f)]
plt.hist(x)
plt.show()

