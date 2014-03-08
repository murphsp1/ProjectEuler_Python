import numpy as np


def read_data(fname):
    #The idiomatic way to handle file reading
    with open(fname, 'r') as file_handle:
        data = []
        for line in file_handle:
            line = line.split(',')
            line = [int(l) for l in line]
            data.append(line)            
    return(data)



def dynamic_min_path(data):

    rows, cols = data.shape



    for r in xrange(rows-1,-1,-1):
        for c in xrange(cols-1,-1,-1):
            data[r,c] += min([data[r+1,c],data[r,c+1]])

    return(data[0,0])


def dynamic_min_path(data, r_start, c_start):

    rows, cols = data.shape
    rows -= 1
    cols -= 1

    #precompute the solution at the boundaries
    for r in xrange(rows-1,-1,-1):
        data[r,cols] += data[r+1,cols]

    for c in xrange(cols-1,-1,-1):
        data[rows,c] += data[rows,c+1]

    for r in xrange(rows-1,-1,-1):
        for c in xrange(cols-1,-1,-1):
            data[r,c] += min([data[r+1,c],data[r,c+1]])
            
    return(data[0,0])



def main()
    #problem
    test_data = [ [ 131, 673, 234, 103, 18],
                    [201, 96,  342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524, 37,  331]]

    #test_data = read_data('matrix_82.txt')
    test_data = np.array(test_data)

    rows, cols = test_data.shape

    for  :
    	new = np.copy(test_data)
    


if __name__ == '__main__':
    main82()
