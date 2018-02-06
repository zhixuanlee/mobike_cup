from mobike_destination_predict.dataprocess.dataprocess.toloc import toloc
import pandas as pd
import time
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.model_selection import train_test_split
from mobike_destination_predict.merge import merge
print('start loading data' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))
train_data = pd.read_csv('F:/data science/data/mobike/traindata.csv')
predict_data = pd.read_csv('F:/data science/data/mobike/testdata.csv')

for r in [2, 8, 16]:
    print('fitting model:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

    X_train, X_test, y_train, y_test = train_test_split(train_data.iloc[:, 0:4],
                                                        train_data.iloc[:, 4:6],
                                                        train_size=0.9,
                                                        random_state=r)

    model = MultiTaskLassoCV(copy_X=True,
                             cv=8,
                             n_jobs=-1).fit(X_train, y_train)

    print('predicting:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

    result = model.predict(predict_data)
    result = toloc(result)
    print('saving result:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

    pd.DataFrame(result).to_csv('F:/data science/data/mobike/result-%d.csv' % r)
    print('finish:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))

    merge()
