#! /usr/bin/python
#coding:utf8
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = 12

date_series = pd.date_range(start='2018-01-01', periods=n, freq="D")
data = {'pv': [10000, 12000, 13000, 11000, 9000, 16000, 10000, 12000, 13000, 11000, 9000, 16000], 'gmv': [100, 90, 120, 150, 200, 80, 100, 90, 120, 150, 200, 80]}
df = pd.DataFrame(data, index=date_series)
ax = df.plot(secondary_y=['gmv'], x_compat=True, grid=True)
ax.set_title("pv-gmv")
ax.set_ylabel('pv')
ax.right_ax.set_ylabel('gmv')
ax.grid(linestyle="--", alpha=0.3)
# plt.show()
plt.savefig('1.jpg')

