import sys

def read_data():
    #The idiomatic way to handle file reading
    with open('data.txt', 'r') as file_handle:
        data = []
        for line in file_handle:
            data.append(int(line))
            
    return(data)



def main():
    data = read_data()
    output = str(sum(data))
    output = output[0:10]
    print(output)



if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
