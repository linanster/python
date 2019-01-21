#! /usr/bin/python
#coding:utf8
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = 12

date_series = pd.date_range(start='2018-01-01', periods=n, freq="D")
data = [10000, 12000, 13000, 11000, 9000, 16000, 10000, 12000, 13000, 11000, 9000, 16000]
df = pd.DataFrame(data, index=date_series)
# ax = df.plot(x_compat=True, grid=True)
ax = df.plot(grid=True)
ax.set_title("test")
ax.set_ylabel('op_rate')
ax.set_label('time_hourly')
ax.grid(linestyle="--", alpha=0.3)
plt.show()
# plt.savefig('1.jpg')

