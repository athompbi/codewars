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


### 4
### Alphanumeric checker

def alphanumeric(password):
    """Checks if a given password is alphanumeric
    
    Return:
        True: if password only contains alphanumeric characters
        False: if password is empty, contains spaces, underscores, or other 
            non-alphanumeric characters. """

    if password == "":
        return False
    
    for x in password:
        if x == " " or x == '_':
            return False
        elif x not in ('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return False
    
    ### added character counter to verify the password contains at least one number

    # character_count = 10

    # for character in ('1234567890'):
    #     if character not in password:
    #         character_count -= 1

    # if character_count == 0:
    #     return False

    else:
        return True


######################################################################


### 5
### ROT13 Cipher

### This is a basic Caeser cipher that I wrote and then altered to 
### create the ROT13 Cipher.

def basic_caeser_cipher(string, n):
    """A basic Caeser cipher that takes a string and then moves
    each letter's ascii by n, giving a new character. This cipher
    only affects letters, all other characters are the same as 
    in the original string. 
    
    Return:
        new_string: string processed through cipher"""

    def get_new_ascii(ascii, n, max):
        """Gets the new ascii for encoding through a cipher. The ascii 
        has n added to it, and if the new ascii is out of range of the max,
        then 26 is subtracted to keep the character a letter.
        
        Return:
            new_ascii: converted ascii"""

        new_ascii = ascii + n
        if new_ascii > max:
            new_ascii -= 26

        return new_ascii

    new_string = ""

    for character in string:

        ascii = ord(character)

        if ascii > 96 and ascii < 123:
            new_string += chr(get_new_ascii(ascii, n, 122))

        elif ascii > 64 and ascii < 91:
            new_string += chr(get_new_ascii(ascii, n, 90))

        else:
            new_string = new_string + character

    return new_string


def rot13(string):
    """A ROT13 cipher that takes a string and then moves
    each letter's ascii by 13, giving a new character. This cipher
    only affects letters, all other characters are the same as 
    in the original string. 
    
    Return:
        new_string: string processed through cipher"""

    def get_new_ascii(ascii, max):
        """Gets the new ascii for processing through the ROT13 cipher. The ascii 
        has 13 added to it, and if the new ascii is out of range of the max,
        then 26 is subtracted to keep the character a letter.
        
        Return:
            new_ascii: converted ascii"""

        new_ascii = ascii + 13
        if new_ascii > max:
            new_ascii -= 26

        return new_ascii

    new_string = ""

    for character in string:

        ascii = ord(character)

        if ascii > 96 and ascii < 123:
            new_string += chr(get_new_ascii(ascii, 122))

        elif ascii > 64 and ascii < 91:
            new_string += chr(get_new_ascii(ascii, 90))

        else:
            new_string = new_string + character

    return new_string


######################################################################


### 6
### Vowel count

def get_count(sentence):
    """Counts the number of vowels in a given string
    
    Return:
        count: vowel count"""

    count = 0
    for letter in sentence:
        if letter in ("aeiouAEIOU"):
            count += 1

    return count


######################################################################


### 7
### List filtering

def filter_list(list):
    """Filters a list of non-negative integers and string
    and filters out the strings.
    
    Return:
        filtered_list: only contains integers"""

    filtered_list = []

    for item in list:
        if isinstance(item, int) == True:
            filtered_list.append(item)

    return filtered_list


######################################################################


### 8
### Replace with alphabet position


def alphabet_position(string):
    """Takes a string and returns a string with all letters replaced with their
    numerical positions in the alphabet. Does not add characters which are not letters.
    Addds a space between each letter positions for readability.
    
    Return:
        positions: string with letters replaced with alphabet position"""

    positions = ""

    for character in string:

        ascii = ord(character)

        ### lower case letters
        if ascii > 96 and ascii < 123:
            position = ascii - 96
            positions += str(position) + " "

        ### upper case letters
        elif ascii > 64 and ascii < 91:
            position = ascii - 64
            positions += str(position) + " "

    if positions == "":
        return ""
    else:
        ### strips off extra space at the end
        return positions.rstrip(positions[-1])


######################################################################

# import math


# def decimal_binary_converter(decimal):
    
#     bits = math.ceil(math.log(decimal, 2))

#     return bits

# print(decimal_binary_converter(8))

# print(math.log(8,2))
