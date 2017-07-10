from pygeohash import decode

def getloc(str[:] x):
    cdef str i
    cdef la = []
    cdef lo = []
    for i in x:
        loc = decode(i)
        la.append(loc[0])
        lo.append(loc[1])

    return la, lo