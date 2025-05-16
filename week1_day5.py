import pandas as pd

#loading the dataset from csv file
df = pd.read_csv("weather_data.csv")
print(df.head(7))

#shape function
print('\nshape of dataset (rows, columns): ', df.shape)

#tail function-> by default it is showing the last 5 values, but if we pass value
# then, it will show last (value=2)values.
print('Tail function:\n',df.tail())

# 1:3  --> start : end-1
print('start index , ending index\n',df[1:4])


# all the column names
print('printing all the column name:\n',df.columns)

# getting a specific column by giving name of column
print('print the day column only:\n' ,df['day'])

#checking the datatype of column by giving column name
print('\n\nData-type of day column\n', type(df['day']))

#more than one column by passing their names
print('day and temperature column:\n' ,df[['day','temperature']])

#***************************************************************************************************************
                                             #Operations on dataframe
#getting the max value in temperature column
print('Maximum value in temperature column is:' ,df['temperature'].max())

#it will return the complete row in which temperature > 32
print('values in column temperature > 32:\n', df[df['temperature']>32])

print(df['day'][df['temperature'] == df['temperature'].max()])

print(df[df['temperature'] == df['temperature'].max()]) # Kinda doing SQL in pandas

print(df['temperature'].std())

print(df['event'].max()) # But mean() won't work since data type is string

print(df.describe())

#****************************************** set index ***************************************************
print(df.set_index('day'))

print(df.set_index('day', inplace=True))

# df.index
# df.loc['1/2/2017']
#
# df.reset_index(inplace=True)
# df.head()
#
# df.set_index('event',inplace=True) # this is kind of building a hash map using event as a key
# df
#
# df.loc['Snow']






