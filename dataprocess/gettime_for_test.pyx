import time

def gettime_for_test(x):
    cdef hour = []
    cdef week = []
    for i in x :
        date = time.strptime(i[0:19], '%Y-%m-%d %H:%M:%S')
        hour.append(date.tm_hour)
        week.append(date.tm_wday)
    return week, hour