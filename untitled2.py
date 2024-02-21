# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F5XhcJa2Elf6L0VO8tnRpQk2-MfF5anA

LINE CHART
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,13,17,20]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.title('Line Chart')
plt.show()

"""BAR CHART"""

import matplotlib.pyplot as plt
categories = ['Catogory A','Catogory B','Catogory c']
values = [25,40,30]
plt.bar(categories,values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()



"""SCATTER PLOT"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,13,17,20]
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()



"""AREA PLOT"""

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,13,17,20]
plt.fill_between(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot')
plt.show()



"""PIE CHART

"""

import matplotlib.pyplot as plt
labels = ['A','B','C','D']
sizes = [15,30,45,10]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

"""TABLE CHART"""

import pandas as pd
data = {
     'Name':['Alice','Bob','Charlie','David'],
     'Age':[25,30,45,36],
     'City':['New york','Los Angeles','Chicago','India']}
df = pd.DataFrame(data)
print(df)

"""POLAR CHART

"""

import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0,2*np.pi,6)
r=[1,2,3,4,5,6]
plt.polar(theta,r)
plt.title('Polar Chart')
plt.show()



"""HISTOGRAM

"""

import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data,bins=20)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

"""LOLLIPOP CHART"""

import matplotlib.pyplot as plt
categories = ['A','B','C','D']
values = [5,10,15,8]
plt.stem(categories, values, basefmt='')
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Lollipop Chart')
plt.show()