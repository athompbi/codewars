######################################################################


### 1
### Playing with digits

def dig_pow(n, p):
    """Given an integer, calculate if k exists such that
    the sum of the digits of n taken to the successive powers of
    p is equal to k * n, else return -1.
    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    
    Return:
        k: sum / n
        -1: if k is not an integer"""

    sum = 0

    for digit in str(n):
        sum += int(digit) ** p
        p += 1

    k = sum / n

    if k.is_integer() == True:
        return int(k)
    else:
        return -1


######################################################################


### 2
### Well of ideas - Easy Version

def well(x):
    """Determines how many 'good' ideas are in a given
    list and returns text based on how many 'good' ideas
    are in the list
    
    Return:
        Text based on number of 'good' ideas in list"""

    good_count = 0

    for item in x:
        if item == 'good':
            good_count += 1
        
    if good_count == 1 or good_count == 2:
        return 'Publish!'
    elif good_count > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'


######################################################################


### 3 
### Hashtag generator

def generate_hashtag(s):
    """Generates a hashtag from a string of text. Adds a '#' symbol, capitalizes 
    the first letter of every word, and removes all spaces. 
    
    Return:
        False: if string is empty or hashtag is longer than 140 characters
        hashtag: generated hashtag"""

    if s == "":
        return False
    
    hashtag = ('#' + s.title()).replace(' ', '')

    if len(hashtag) > 140:
        return False
    else:
        return hashtag


######################################################################


# import math


# def decimal_binary_converter(decimal):
    
#     bits = math.ceil(math.log(decimal, 2))

#     return bits

# print(decimal_binary_converter(8))

# print(math.log(8,2))
