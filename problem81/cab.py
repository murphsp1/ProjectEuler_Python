import numpy as np


XMAX = 20
YMAX = 20


def read_data(fname):
    #The idiomatic way to handle file reading
    with open(fname, 'r') as file_handle:
        data = []
        for line in file_handle:
            line = line.split(' ')
            line = [int(l) for l in line]
            data.append(line)            
    return(data)


def paths(x=0, y=0):

    if (x== XMAX) and (y==YMAX):
        return 1
    elif (x==XMAX):
        return paths(x, y+1)
    elif (y==YMAX):
        return paths(x+1, y)
    else:
        return paths(x+1, y) + paths(x, y+1)


def paths2(x=0, y=0):

    if (x== XMAX) or (y==YMAX):
        return 1
    else:
        return paths2(x+1, y) + paths2(x, y+1)



def paths_reverse(x = XMAX, y = YMAX, prcount=0):
    print prcount
    if (x==0) or (y==0):
        return 1
    else:
        return paths_reverse(x-1,y, prcount+1) + paths_reverse(x, y-1, prcount+1)



path_store = np.zeros([YMAX+1, XMAX+1])

def paths_reverse_memoized(x = XMAX, y = YMAX):

    if (x==0) or (y==0):
        return 1
    else:
        if path_store[y,x]>0:
            print 'memoized'
            return path_store[y,x]
        else:
            p1 = paths_reverse_memoized(x-1,y)
            #path_store[y,x-1] = p1
            p2 = paths_reverse_memoized(x, y-1)
            #path_store[y-1, x] = p2
            path_store[y,x] = p1 + p2
            return p1 + p2






def main():
    test_data = [ [ 131, 673, 234, 103, 18],
                    [201, 96,  342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524, 37,  331]]

    data = read_data('matrix_81.txt')
    print paths()
    print paths2()
    print paths_reverse()
    print paths_reverse_memoized()






if __name__ == '__main__':
    main()
