from mobike_destination_predict.dataprocess.dataprocess.getloc import getloc
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import MultiTaskLassoCV

print('start loading data' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
train_data = pd.read_csv('F:/data science/data/mobike/train.csv')
predict_data = pd.read_csv('F:/data science/data/mobike/test.csv')

print('processing data' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
del train_data['orderid']
del train_data['userid']
del train_data['bikeid']
del train_data['starttime']
train_data['startla'], train_data['startlo'] = getloc(train_data['geohashed_start_loc'])
train_data['endla'], train_data['endlo'] = getloc(train_data['geohashed_end_loc'])
del train_data['geohashed_start_loc']
del train_data['geohashed_end_loc']

del predict_data['orderid']
del predict_data['userid']
del predict_data['bikeid']
del predict_data['starttime']
predict_data['startla'], predict_data['startlo'] = getloc(predict_data['geohashed_start_loc'])
del predict_data['geohashed_start_loc']

print('fitting model:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

X_train, X_test, y_train, y_test = train_test_split(train_data.iloc[:, 0:3],
                                                    train_data.iloc[:, 4:5],
                                                    train_size=0.7,
                                                    random_state=2)
print(X_train.shape)
print(X_train.shape)
print(X_test.shape)
model = MultiTaskLassoCV(copy_X=True, cv=8, n_jobs=-1).fit(X_train, y_train)
print('predicting:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

result = model.predict(predict_data)

print('saving result:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

result.tocsv('F:/data science/data/mobike/result-1.csv')
print('finish:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
