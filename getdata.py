import pandas as pd
import time
from getweek import getweeks
from getloc import getloc

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
data = pd.read_csv('F:\data science\data\mobike\\test.csv', index_col=None, header=0)

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
data['orderid'], data['userid'] = getweeks(data['starttime'].values)

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
del data['bikeid']
del data['biketype']
del data['starttime']

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
data['starla'], data['starlo'] = getloc(data['geohashed_start_loc'].values)
data['endla'], data['endlo'] = getloc(data['geohashed_end_loc'].values)

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
del data['geohashed_start_loc']
del data['geohashed_end_loc']
data.columns = ['tm_week', 'tm_hour', 'st_la', 'st_lo', 'en_la', 'en_lo']

print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
data.to_csv('F:\data science\data\mobike\\test2.csv')


print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))