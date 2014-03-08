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


#the recursive solution below will not work because
#Python has a recursive depth limit set to 1000 (which could be changed)
#and, more importantly, I am appending and growing the min_sum list
#to astronomical size
#I still have the question as to how to not do it this way ... ie
#do not grow the min_sum list and instead just keep track of the smallest
#path sum that I have found so far

def min_path(data, min_sum, x, y, acc=0):

    acc += data[x,y]
    if (x == 0) and (y==0):
        min_sum.append(acc)
        return acc
    
    if (y>=0):
        min_path(data, min_sum, x, y-1, acc)

    if (x>=0):
        min_path(data, min_sum, x-1, y, acc)

#the dynamic programming solution is by far the better approach
#here and I did something similar back in problem 18
#starting from the bottom corner, back compute the smallest path
#at each step and rebuild my own matrix of smallest paths

def dynamic_min_path(data):

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



def main():
    #problem 81
    test_data = [ [ 131, 673, 234, 103, 18],
                    [201, 96,  342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524, 37,  331]]

    #test_data = read_data('matrix_81.txt')
    test_data = np.array(test_data)
    dynamic_min_path(test_data)

    #XMAX, YMAX = test_data.shape
    #mins = []
    #print min_path(test_data, mins, x=XMAX-1, y=YMAX-1, acc=0)


    


if __name__ == '__main__':
    main()


