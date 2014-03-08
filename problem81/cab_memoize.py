import numpy as np


XMAX = 3
YMAX = 3


path_store = np.zeros([YMAX, XMAX])
path_store[0,0] = 0
path_store[1,0] = 1
path_store[0,1] = 1


def paths(x=XMAX-1, y=YMAX-1):


    p1 = 0
    p2 = 0

    if (y>0):
        if path_store[y-1,x]>0:
            p1 = path_store[y-1,x]
        else:
            p1 = paths(x, y-1) + 1
            path_store[y-1,x] = p1



    if (x>0):
        if path_store[y,x-1]>0:
            p2 = path_store[y, x-1]
        else:
            p2 = paths(x-1, y) + 1
            path_store[y, x-1] = p2


    return p1 + p2


def main():
    num_paths = paths()
    print num_paths





if __name__ == '__main__':
    main()