from os import path
from os import getcwd
import pandas
from pandas import DataFrame
from scipy import stats
import numpy
import matplotlib
import seaborn
seaborn.set()
from pandas.tools import plotting

# categorical vs numeric values: easier to group by categorical values.

# LOAD CSV FILE INTO PANDAS
myfile = path.join(getcwd(), 'brain_size.csv')
print(myfile)
data = pandas.read_csv(myfile, sep=';', na_values='.')
# can also read_  clipboard, csv, xml, json, html, sql_table
# print(data)
print(data.shape)  # (#rows, #columns)
print(data.columns)

# SELECTS AND FILTERS
gender_column = data['Gender']
print(gender_column)
# print(data[gender_column == 'Female']) # all rows and columns from data where Gender == Female
female_data = data[gender_column == 'Female']
print(female_data)
viq_for_females = female_data['VIQ']
print(viq_for_females)

# SELECT MULTIPLE COLUMNS USING LIST OF COLUMN NAMES
some_columns = data[['Weight', 'Height', 'MRI_Count']]
print(some_columns)

# PANDAS AGGREGATES
mean_female_viq = viq_for_females.mean()
print(mean_female_viq)
mean_female_viq = viq_for_females.mean()
print('mean_female_viq = ', mean_female_viq)
median_female_viq = viq_for_females.median()
print('median_female_viq = ', median_female_viq)
max_female_viq = viq_for_females.max()
print('max_female_viq = ', max_female_viq)
min_female_viq = viq_for_females.min()
print('min_female_viq = ', min_female_viq)
print(data['VIQ'].mean())


# GROUP BY
groupby_gender = data.groupby('Gender')
print(groupby_gender)  # just an object

for gender, value in groupby_gender['VIQ']:
     print((gender, value.mean()))

print(groupby_gender.mean())  #mean of all values
print(groupby_gender.median())
print(groupby_gender.max())
print(groupby_gender.sum())
print(groupby_gender.count())

# TESTING SIMILARITY
result = stats.ttest_1samp(data['VIQ'], 115)  #  probability of data equalling a given number using normal (gaussian) distribution
print(result)
# matplotlib.interactive(False)
# matplotlib.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

# PANDAS PLOTTING SCATTER MATRIX
from pandas.tools.plotting import scatter_matrix
# df = DataFrame(numpy.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
# scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
# matplotlib.pyplot.show()

# SEABORN
seaborn.pairplot(data, hue="Gender")
seaborn.plt.show()

# COMPARE STATISTICALLY
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
print(stats.ttest_ind(female_viq, male_viq))
print(stats.ttest_rel(data['PIQ'], data['FSIQ']))
print(stats.ttest_ind(data['PIQ'], data['FSIQ']))
print(stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0))
print(stats.wilcoxon(data['FSIQ'], data['PIQ']))

# NUMPY
x = numpy.linspace(-5, 5, 20)  # list containing -5 to +5 in 20 equal steps - note 21 would be better..
print(x)
numpy.random.seed(1)  # is this needed?
# normal distributed noise
y = -5 + 3*x + 4 * numpy.random.normal(size=x.shape) # list containing...
print(y)
# Create a data frame containing all the relevant variables
xy_data = pandas.DataFrame({'x': x, 'y': y})
scatter_matrix(xy_data, alpha=0.2, figsize=(6, 6), diagonal='kde')
matplotlib.pyplot.show()

# which package does statsmodel come from?
# from statsmodels.formula.api import ols
# model = ols("y ~ x", data).fit()

newdata = pandas.DataFrame({'col1': [1,2,3], 'col2': ['a', 'b', 'c']})
print(newdata)
col1 = newdata['col1']
print(col1)

# MELT CREATES SKINNY TABLES
df = pandas.DataFrame({'SensorA':[1,3,4,5,6], 'SensorB':[5,2,3,6,7], 'SensorC':[7,4,8,1,10], 'group_id':[1,2,1,1,2]})
# print(df)
df = pandas.melt(df, id_vars = 'group_id', var_name = 'Sensor')
# print(df)
print(data)
df = pandas.melt(data, id_vars='id', var_name='data')
# print(df)

# REDUCE NUMBER OF COLUMNS BY DROPPING COLUMNS
small_df = data.drop(['MRI_Count', 'PIQ', 'VIQ'], axis=1)
print(small_df)

# REDUCE NUMBER OF COLUMNS BY SELECTING COLUMNS
# AND CUT DOWN ROWS WITH FILTER ON DATA AND FILETER ON INDEX
small_df2 = pandas.DataFrame(
     data[data['Gender'] == 'Female'],
     columns=['id', 'Gender', 'FSIQ', 'Height'],
     index=range(0, 5))
print(small_df2)

# RANGE OF DATES
# B = business day
# D = day (default)
# M = month
# W = week
print(pandas.date_range('20130101', periods=5, freq='W'))

# SINGLE COLUMN WITH INDEX FOR CONCATENATION
one_column = data['FSIQ']
print(one_column)

# CONCAT
data_fisq = pandas.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pandas.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pandas.concat((data_fisq, data_piq))
print(data_long)

# from statsmodels.formula.api import ols
# model = ols("iq ~ type", data_long).fit()
# print(model.summary())

# CLASSIC SEABORN IRIS COMPARISON
# df = seaborn.load_dataset("iris")
# seaborn.pairplot(df, hue="species")

# NICE - SEABORN - SELECT ONLY CERTAIN COLUMNS FOR PAIRPLOT
# CAREFUL - DON'T TRY TO PLOT CATEGORICAL VALUES
# print(data)
# seaborn.plt.rcdefaults()  # set back to default pyplot look and feel
# seaborn.pairplot(data, vars = ['FSIQ', 'VIQ'], hue="Gender")  # if you miss hue="Gender" you get error max must be larger than min in range parameter
# seaborn.plt.show()
# Seaborn uses matplotlib.  matplotlib uses pyplot...
# seaborn.plt refers to pyplot library
# from matplotlib import pyplot as plt

# LINEAR REGRESSION PLOT - 2 VARIABLES
# seaborn.lmplot(y='FSIQ', x='VIQ', data=data)
# seaborn.plt.show()

# robust=True should remove outliers, but needs statsmodel library
# seaborn.lmplot(y='FSIQ', x='VIQ', data=data, robust=True)
# seaborn.plt.show()

