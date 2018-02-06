from keras.models import Sequential
from keras.layers import Dense,Activation
import pandas as pd
import keras
import time

from keras.utils import np_utils

print('start loading data' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
train_data = pd.read_csv('F:/data science/data/mobike/traindata.csv')
predict_data = pd.read_csv('F:/data science/data/mobike/predictdata.csv')
X_train = train_data.iloc[:, 1:4]
y_train = train_data.iloc[:, 4:5]

y_train = np_utils.to_categorical(y_train)

print('building model' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
modle = Sequential()
modle.add(Dense(units=10, input_dim=3))
modle.add(Activation('relu'))

modle.add(Dense(units=10))
modle.add(Activation('relu'))

modle.add(Dense(41))
modle.add(Activation('softmax'))

modle.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='sgd')

print('fitting' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
modle.fit(X_train.values,
          y_train,
          epochs=40)

print('prediceting' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
result = modle.predict(predict_data.iloc[:, 1:4].values)
result = pd.DataFrame(result)
result.to_csv('F:/data science/data/mobike/resualt.csv')




