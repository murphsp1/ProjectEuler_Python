import sys

number_names = { 1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
         10: "ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety" }


def construct_double_digit_name(n):
    '''this function computes all word names for numbers for 21 to 99'''
    digits = str(n)

    #grab ten's digit name first
    key = ((int(digits[0]))*10)
    tens_name = number_names[key]

    if digits[1]=='0':
        ones_name = ''
    else:
        ones_name = number_names[int(digits[1])]
        
    name = tens_name + ones_name

    return(name)

def construct_triple_digit_name(n):
    digits = str(n)

    tens = int(digits[1:3])
    #Case for 100, 200, 300, etc
    if tens==0:
        name = number_names[int(digits[0])] + "hundred"
    else:
        hundreds_name = number_names[int(digits[0])] + "hundredand"
        if tens<21:
            second_name = number_names[tens]
        else:
            second_name = construct_double_digit_name(tens)
        name = hundreds_name+second_name

    return(name)



def construct_name_from_number(n):
    if n <21:
        name = number_names[n]
    elif n<100:
        name = construct_double_digit_name(n)
    elif n<1000:
        name = construct_triple_digit_name(n)
    else:
        name = "onethousand" 

    return(name)



def main():
    stop = 1000
    count = 0
    for i in xrange(1,stop+1):
        name = construct_name_from_number(i)
        print(name)
        count = len(name) + count


    print(count)


if __name__ == '__main__':
    #call function that we need


    sys.exit(main())


