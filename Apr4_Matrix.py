from numpy import *
a = ([['Rhia',10,20,30,40,50],
['Alan',75,80,75,85,100],
['Smith',80,80,80,90,95]])


b = array(a)
b[0:3, 0:2].tolist()


a[2] = ['Sam',82,79,88,97,99]

a[0][4] = 95


a = np.insert(a, 6, (73,80,85),axis=1)
