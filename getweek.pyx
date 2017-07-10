import time

def getweeks(str[:] x):
    cdef week = []
    cdef hour = []
    cdef int i

    for i in range(len(x)):
        the_time = time.strptime(x[i], '%Y-%m-%d %H:%M:%S')
        week.append(the_time.tm_wday)
        hour.append(the_time.tm_hour)


    return week, hour
