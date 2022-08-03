######################################################################


### 1
### Multiples of 3 or 5

def solution(number):
    """Finds all multiples of 3 and 5 below a given number
    and adds them together
    
    Return:
        sum = sum of multiples of 3 and 5"""

    def find_multiples(number, divisor):
        """Finds all the multiples of a number. Takes the number and determines
        if there are any remainders after dividing by calculating multiple.
        Then lists multiples and adds to a list of multiples
        
        Return:
            multiples_list: list of multiples"""

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


######################################################################


### 2
### Printer errors

def printer_error(s):
    """Determines the number of printer errors in a string
    (errors are characters outside of a-m)
    
    Returns: 
        error_rate: number of errors / string length"""

    denominator = len(s)
    numerator = 0

    for letter in s:
        if letter in ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'):
            pass
        else:
            numerator = numerator + 1

    error_rate = (f'"{numerator}/{denominator}"')

    return error_rate


######################################################################


### 3
### Disemvowel Trolls

def disemvowel(string_):
    """Removes vowels from a string
    
    Returns: 
        string_: string without vowels"""

    string_list = []

    for letter in string_:
        if letter in ("aeiou"):
            pass
        else:
            string_list.append(letter)

    string_ = ''.join(string_list)

    return string_


######################################################################


### 4
### Create phone number

def create_phone_number(n):
    """Takes a 10 digits number and formats it to a phone number
    
    Returns: 
        phone_number: formatted phone number
    """

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


######################################################################


### 5
### Narcissistic Number

def narcissistic(number):
    """Determines if a number is narcississtic (the sum of the digits to the power of 
    the number length equal the number)
    
    Return:
        is_narcissistic: Boolean if number is narcissistic"""
        
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


######################################################################


### 6
### Array difference

def array_diff(a, b):
    """Determines which elements are in array a, but not in array b.
    Creates new array of elements only in a.
    
    Return:
        c: new list of items only in a and not in b"""

    c = []
    for item in a:
        if item not in b:
            c.append(item)
        
    return c


######################################################################


### 7
### Twice as old

def twice_as_old(dad_age,son_age):
    """Solves a riddle determining how many years 
    away a dad's current age to his son's current age doubled
    
    Return: 
        Solution to the riddle"""

    return abs(son_age * 2 - dad_age)


######################################################################


### 8
### Remove first and last characters

def remove_char(string):
    """Removes the first and last characters of a string
    
    Return:
        String without first and last characters"""

    string_list = []

    for letter in string:
        string_list.append(letter)

    string_list.pop(-1)
    string_list.pop(0)

    return ''.join(string_list)
    

######################################################################


### 9
### Human Readable Time

def human_readable_time(seconds):
    """Takes a time in seconds and converts it to HH:MM:SS
    
    Return:
        HH:MM:SS"""

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


######################################################################


### 10
### Who likes it?

def likes(names):
    """Takes a list of names and returns text based on how many
    people are in the list. Can be used for something like displaying
    facebook likes.
    
    Return:
        Text of who likes this"""

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


######################################################################