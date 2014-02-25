import sys



alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = [i for i in alphabet]

def read_data():
    #The idiomatic way to handle file reading
    with open('names.txt', 'r') as file_handle:
        data = []
        for line in file_handle:
            data.append(line)
            
    return(data)

def compute_alphabetical_value(name):
    value = 0
    for letter in name:
        value += alphabet.index(letter)+1

    return(value)


def main():
    data = read_data()
    names = data[0].split(',')
    names = [n[1:-1] for n in names]
    names.sort()

    total_score = 0
    for i,name in enumerate(names):
        name_value = compute_alphabetical_value(name)
        total_score += (name_value * (i+1))

    print(total_score)






if __name__ == '__main__':
    #call function that we need


    sys.exit(main())
