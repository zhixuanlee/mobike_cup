import pandas

a = pandas.read_csv('F:/data science/data/mobike/test.csv')
b = pandas.read_csv('F:/data science/data/mobike/result-1.csv')
c = pandas.read_csv('F:/data science/data/mobike/result-2.csv')
d = pandas.read_csv('F:/data science/data/mobike/result-3.csv')

del a['bikeid']
del a['userid']
del a['biketype']
del a['starttime']
del a['geohashed_start_loc']
a['loc1'] = b['0']
a['loc2'] = c['0']
a['loc3'] = d['0']
a.to_csv('F:/data science/data/mobike/result.csv', index=None, header=None)