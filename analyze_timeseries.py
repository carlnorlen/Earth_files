import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("MOD11A2-006-Statistics-LST-2.csv")
monthly_avg_temp = df.groupby(["Year", "Month"])["Mean-C"].mean()
yearly_avg_temp = df.groupby(["Year"])["Mean-C"].mean()
pd.DataFrame(yearly_avg_temp).plot.bar()
pd.DataFrame(yearly_avg_temp).plot.line()

years = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', 
'2009', '2010', '2011', 
	'2012', '2013', '2014', '2015', '2016', '2017', '2018']
x_pos = np.arange(len(years))

fig, ax = plt.subplots()

ay.set_yticks(
ax.set_xticks(x_pos)
ax.set_xticklabels(years)
ax.set_ylabel('Yearly Temperature, C')
ax.set_title('Pattern of Land Surface Temperature, Southern California, 
2001-2018')
plt.show()

#y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#x_pos = np.arange(len(months))

#pd.DataFrame(monthly_average_temperature).plot.bar()
#pd.DataFrame(monthly_average_temperature).plot.line()
#plt.show()
