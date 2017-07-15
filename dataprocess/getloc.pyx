from pygeohash import decode

def getloc(x):
    cdef la = []
    cdef lo = []
    cdef str i
    for i in x:
        la.append(decode(i)[0])
        lo.append(decode(i)[1])

    return la, lo