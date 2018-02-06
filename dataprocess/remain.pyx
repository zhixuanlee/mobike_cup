def remain(x):
    cdef int i
    for i in range(len(x)):
        print(i)
        x[i] = x[i][0:7]
        print(x[i])

    return x

