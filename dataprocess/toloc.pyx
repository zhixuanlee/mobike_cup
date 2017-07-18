from pygeohash import encode

def toloc(x):
    cdef loc = []
    cdef i = int
    for i in range(len(x)):
        loc.append(encode(x[i,0], x[i,1]))

    return loc