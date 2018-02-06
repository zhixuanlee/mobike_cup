from pygeohash import decode_exactly

def getloc(x):
    cdef la = []
    cdef lo = []
    cdef str i
    for i in x:
        la.append(decode_exactly(i)[0])
        lo.append(decode_exactly(i)[1])

    return la, lo