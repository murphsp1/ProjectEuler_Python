import sys
import operator as o

window = 4

def read_data():
    #The idiomatic way to handle file reading
    with open('data.txt', 'r') as file_handle:
        data = []
        for line in file_handle:
            l = line.split(' ')
            d= [int(x) for x in l]
            data.append(d)
            
    return(data)

def horizontal_search(data):
    max_value = 0
    for row in data:
        i = 0
        while i+window < len(row):
            new_val = reduce(o.mul, row[i:i+window],1)
            max_value = max(max_value, new_val)
            i += 1
    return max_value

def vertical_search(data):
    max_value = 0
    return max_value

def diagonal_search(data):
    max_value = 0
    r = 0
    while r+window<len(data):
        c = 0
        while c+window<len(data[r]):
            new_val = data[r][c]*data[r+1][c+1]*data[r+2][c+2]*data[r+3][c+3]
            max_value = max(max_value, new_val)
            c = c + 1
        r = r + 1
    return max_value

def main():
    data = read_data()
    max_horizontal = horizontal_search(data)
    print(max_horizontal)

    #being lazy
    data_transposed = zip(*data)
    data_transposed = [list(l) for l in data_transposed]
    max_vertical = horizontal_search(data_transposed)
    print(max_vertical)


    max_diag1 = diagonal_search(data)
    print(max_diag1)

    max_diag2 = diagonal_search(data_transposed)
    print(max_diag2)

    data_flipped = []
    for row in data:
        new_row = [i for i in reversed(row)]
        data_flipped.append(new_row)
    max_diag3 = diagonal_search(data_flipped)
    print(max_diag3)

    #for vertical search, I might just cheat and transpose things
    #this would be far easier with numpy


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


max_prod = 0
for i in range(20):
    for j in range(16):
        # up/down products
        prod = M[j][i]*M[j+1][i]*M[j+2][i]*M[j+3][i]
        if prod > max_prod: max_prod = prod

for i in range(20):
    for j in range(16):
        # right/left products
        prod = M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]
        if prod > max_prod: max_prod = prod


max_prod = 0
for i in range(16):
    for j in range(16):
        prod = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
        if prod > max_prod: max_prod = prod

