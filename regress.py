import pandas  as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import MultiTaskLassoCV
import time

data = pd.read_csv('F:\data science\data\mobike\\traindata.csv', header=None, index_col=None)

X_train, X_test, y_train, y_test = train_test_split(data.loc[:, 0:3], data.loc[:, 4:5], test_size=0.33, random_state=2)

print('start fitting')
print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
model = MultiTaskLassoCV(normalize=True, copy_X=True, n_jobs=-1, random_state=2).fit(X_train, y_train)
print('finish')
print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
print(model.score(X_test, y_test))
print(model.predict(X_test)-y_test)
print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
