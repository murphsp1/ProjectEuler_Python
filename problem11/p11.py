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
    return max_value

def main():
    data = read_data()
    max_horizontal = horizontal_search(data)
    print(max_horizontal_value)

    #being lazy
    data_transposed = zip(*data)
    data_transposed = [list(l) for l in data_transposed]
    max_vertical = horizontal_search(data_transposed)
    max_vertical

    #for vertical search, I might just cheat and transpose things
    #this would be far easier with numpy


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
