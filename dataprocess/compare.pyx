#cython: boundscheck=False, wraparound=False, nonecheck=False
import time
def compare(x, y):
    cdef int i = 0
    cdef int n = 1
    for i in y.index:
        try:
            print(i)
            y.ix[i, 'loc1'] = x.ix[i, 'geohashed_end_loc']
            print('============%d====================',n)
            n += 1
        except:
            pass
    return y