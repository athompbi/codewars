###################################################################
### Multiples of 3 or 5

def solution(number):

    def find_multiples(number, divisor):

        remainder = number % divisor

        if remainder == 0:
            highest_mult = number - divisor
        else:
            highest_mult = number - remainder

        while highest_mult > 0:

            if highest_mult in multiples_list:
                pass
            else:       
                multiples_list.append(highest_mult)
            
            highest_mult = highest_mult - divisor

    multiples_list = []

    find_multiples(number,3)
    find_multiples(number,5)

    sum = 0

    for num in multiples_list:
        sum += num

    return sum


#######################################################################
### Printer errors

def printer_error(s):
    denominator = len(s)
    numerator = 0

    for letter in s:
        if letter in ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'):
            pass
        else:
            numerator = numerator + 1

    error_rate = (f'"{numerator}/{denominator}"')
    print(error_rate)
    return error_rate


##################################################################
### Disemvowel Trolls

def disemvowel(string_):

    string_list = []

    for letter in string_:
        if letter in ("aeiou"):
            pass
        else:
            string_list.append(letter)

    string_ = ''.join(string_list)

    return string_


#####################################################################
### Create phone number

def create_phone_number(n):
    n = str(n)
    one = n[0]
    two = n[1]
    three = n[2]
    four = n[3]
    five = n[4]
    six = n[5]
    seven = n[6]
    eight = n[7]
    nine = n[8]
    ten = n[9]
    phone_number = (f'({one}{two}{three}) {four}{five}{six}-{seven}{eight}{nine}{ten}')
    return phone_number

################################################################
### Narcissistic Number

def narcissistic(number):
    number = str(number)
    sum = 0

    length = len(number)
    is_narcissistic = False

    for x in number:
        y = int(x) ** length
        sum = sum + y

    if str(sum) == number:
        is_narcissistic = True
    else:
        is_narcissistic = False

    return is_narcissistic

###################################################################
### Array difference

def array_diff(a, b):
    c = []
    for item in a:
        if item not in b:
            c.append(item)
        
    return c

#####################################################################
### Twice as old

def twice_as_old(dad_age,son_age):

    return abs(son_age * 2 - dad_age)

#####################################################################
### Remove first and last characters

def remove_char(string):

    string_list = []

    for letter in string:
        string_list.append(letter)

    string_list.pop(-1)
    string_list.pop(0)

    return ''.join(string_list)
    
####################################################################
### Human Readable Time

# 1 hour, 1 minute, 1 seconds = 3661

def human_readable_time(seconds):

    hours = int(seconds / 3600)

    seconds = seconds - hours * 3600

    minutes = int(seconds / 60)

    seconds = seconds - minutes * 60

    if hours < 10:
        hours = (f'0{hours}')
    
    if minutes < 10:
        minutes = (f'0{minutes}')

    if seconds < 10:
        seconds = (f'0{seconds}')

    return (f'{hours}:{minutes}:{seconds}')

print(human_readable_time(5))

###################################################################
### Who likes it?

def likes(names):
    if len(names) == 0:
        return ('no one likes this')
    if len(names) == 1:
        return (f'{names[0]} likes this')
    if len(names) == 2:
        return (f'{names[0]} and {names[1]} like this')
    if len(names) == 3:
        return (f'{names[0]}, {names[1]} and {names[2]} like this')
    if len(names) >= 4:
        return (f'{names[0]}, {names[1]} and {len(names) -2} others like this')


