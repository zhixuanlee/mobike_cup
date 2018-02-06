import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.model_selection import train_test_split,learning_curve
import numpy as np
import tensorflow as tf


def nn(train, label, train_t, label_t, test, num_label):
    n = train.shape[1]
    x = tf.placeholder('float')
    w1 = tf.Variable(tf.truncated_normal([n, 10], stddev=0.1))
    b1 = tf.Variable(tf.truncated_normal([10], stddev=0.1))
    h1 = tf.sigmoid(tf.matmul(x, w1) + b1)

    w2 = tf.Variable(tf.truncated_normal([10, 10], stddev=0.1))
    b2 = tf.Variable(tf.truncated_normal([10], stddev=0.1))
    h2 = tf.sigmoid(tf.matmul(h1, w2) + b2)

    w3 = tf.Variable(tf.truncated_normal([10, 10], stddev=0.1))
    b3 = tf.Variable(tf.truncated_normal([10], stddev=0.1))
    h3 = tf.nn.relu(tf.matmul(h1, w3) + b3)

    k_p = tf.placeholder('float')
    h3_drop = tf.nn.dropout(h3, k_p)

    w4 = tf.Variable(tf.truncated_normal([10, num_label], stddev=0.1))
    b4 = tf.Variable(tf.truncated_normal([num_label], stddev=0.1))
    y = tf.nn.softmax(tf.matmul(h1, w4) + b4)

    y_ = tf.placeholder(float)
    init = tf.initialize_all_variables()

    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    sess = tf.Session()
    sess.run(init)

    with tf.Session() as sess:
        sess.run(init)
        for i in range(len(x)):
            try:
                batch = [train[i:i + 50], label[i:i + 50]]
            except:
                pass
            if i % 100 == 0:
                train_accuracy = accuracy.eval(feed_dict={
                    x: batch[0], y_: batch[1], k_p: 1.0})
                print("step %d, training accuracy %g" % (i, train_accuracy))
            train_step.run(feed_dict={x: batch[0], y_: batch[1], k_p: 0.5})
        print("test accuracy %g" % accuracy.eval(feed_dict={
            x: train_t, y_: label_t, k_p: 1.0}))

        pre = sess.run(y, feed_dict={x: test})

        return pre

if __name__ == '__main__':
    train_data = pd.read_csv('F:/data science/data/mobike/traindata.csv')
    predict_data = pd.read_csv('F:/data science/data/mobike/testdata.csv')

    y_2 = pd.read_csv('F:/data science/data/mobike/train.csv')

    X_train, X_test, y_train, y_test = train_test_split(train_data.iloc[:, 0:4],
                                                            train_data.iloc[:, 4:6],
                                                            train_size=0.5,
                                                            random_state=1)
    print('fitting model:' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec))


    to_num = pd.get_dummies(y_2['geohashed_end_loc'])
    print(to_num)
    num_label = len(pd.get_dummies(y_2['geohashed_end_loc']).columns)
    print(pd.get_dummies(y_2['geohashed_end_loc']).columns)
    pre = nn(X_train, y_train, X_test, y_test, predict_data)
    pre = pd.DataFrame(pre)

    pre.to_csv('F:/data science/data/mobike/resualt_nn.csv')
