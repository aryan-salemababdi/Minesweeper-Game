# develop by aryan salemabadi 9927073
import numpy as np
file= open(r'A:/project & example python/example/soale 3/matrix.txt',mode = 'r')
w = file.read()
y = w.count('\n')+1
x = len(w.replace(' ','').split('\n'))
l = w.replace('\n',' ').split()
ar = np.array(l)
ar = ar.reshape(y,x)
ar = ar.astype(int)
r = np.zeros((x,y))
for y_pos in range(0, y):
    for x_pos in range(0, x):
        adj_squares = ar[max((y_pos)-1,0):min(y, y_pos+2), max((x_pos-1),0):min(x, x_pos+2)]
        if ar[y_pos,x_pos]==1:
            count = adj_squares.sum()-1
        else:
            count = adj_squares.sum()
        r[y_pos, x_pos]=str(count)
print(r)