# coding:utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 怎么显示中文:
# 1. 找到matplotlibrc文件： 
# import matplotlib 
# print(matplotlib.matplotlib_fname()) 
# 2. 去掉 font.family和font.sans-serif的注释
# 3. 在font.sans-serif那行加上SimHei
# 4. 重启python

continent_en = ["North america", "South america", "Europe", "Asia", "Oceania", "Africa", "Antarctica"]
continent_ch = ["北美洲", "南美洲", "欧洲", "亚洲", "大洋洲", "非洲", "南极洲"]
sales = [1500, 500, 1500, 2000, 1000, 500, 1]

# split the figure 
fig, (axis1,axis2) = plt.subplots(nrows=2, ncols=1)
# vertical 
axis1.bar(continent_ch, sales)
# horizontal
axis2.barh(continent_en, sales)
plt.show()