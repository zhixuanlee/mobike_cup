import pandas as pd
from mobike_destination_predict.dataprocess.dataprocess.getloc import getloc
from mobike_destination_predict.dataprocess.dataprocess.gettime import gettime
from mobike_destination_predict.dataprocess.dataprocess.gettime_for_test import gettime_for_test

print('load')
train = pd.read_csv('F:/data science/data/mobike/train.csv')
test = pd.read_csv('F:/data science/data/mobike/test.csv')

print('train')
train['week'], train['hour'] = gettime(train['starttime'])
train['startla'], train['startlo'] = getloc(train['geohashed_start_loc'])
train['endla'], train['endlo'] = getloc(train['geohashed_end_loc'])

print('del')
del train['orderid']
del train['userid']
del train['bikeid']
del train['biketype']
del train['starttime']
del train['geohashed_start_loc']
del train['geohashed_end_loc']
print('save')
train.to_csv('F:/data science/data/mobike/traindata.csv', index=None)

print('test')

test['week'], test['hour'] = gettime_for_test(test['starttime'])
test['startla'],test['startlo'] = getloc(test['geohashed_start_loc'])

print('del')
del test['orderid']
del test['userid']
del test['bikeid']
del test['starttime']
del test['biketype']
del test['geohashed_start_loc']
print('save')

test.to_csv('F:/data science/data/mobike/testdata.csv', index=None)