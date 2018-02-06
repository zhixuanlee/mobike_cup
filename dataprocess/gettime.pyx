import time

def gettime(x):
    cdef hour = []
    cdef week = []
    for i in x :
        date = time.strptime(i, '%Y-%m-%d %H:%M:%S')
        hour.append(date.tm_hour)
        week.append(date.tm_wday)
    return week, hour