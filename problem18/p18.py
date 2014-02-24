import sys



def read_data(fname):
    #The idiomatic way to handle file reading
    with open(fname, 'r') as file_handle:
        data = []
        for line in file_handle:
            line = line.split(' ')
            line = [int(l) for l in line]
            data.append(line)            
    return(data)

def back_compute_best_row(row):
    #given a list of numbers, this function returns
    i = 0 
    len_row = len(row)
    best_option = [0] * (len_row-1)
    while i < (len_row-1):
        best_option[i] = max(row[i], row[i+1])
        i += 1

    print(best_option)
    return(best_option)


def main():
    triangle = read_data('triangle67.txt')
    new_triangle = triangle

    i = len(triangle)-1

    while i > 0:
        row = new_triangle[i]
        best_option = back_compute_best_row(row)
        if i-1>=0:
            for j,r in enumerate(new_triangle[i-1]):
                new_triangle[i-1][j] = new_triangle[i-1][j] + best_option[j]
        i = i-1

    print(new_triangle)
    print(new_triangle[0])



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
