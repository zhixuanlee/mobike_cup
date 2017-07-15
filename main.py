from mobike_destination_predict.dataprocess.getloc import getloc
import pandas as pd

train_data = pd.read_csv('F:/data science/data/mobike/train.csv')
predict_data = pd.read_csv('F:/data science/data/mobike/test.csv')

del train_data[['orderid, userid, bikeid, starttime']]
train_data['startla'], train_data['startlo'] = getloc(train_data['geohashed_start_loc'])
train_data['endla'], train_data['endlo'] = getloc(train_data['geohashed_end_loc'])
del train_data[['geohashed_start_loc', 'geohashed_end_loc']]

