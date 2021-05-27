# Ciphers the inputted message
import random

def chartSetter(alphabet):
    # Use the alphabet provided to create a 26 X 26 array

    chart = [["" for i in range(26)] for j in range(26)]

    a = 0
    b = 0
    for x in range(26):
        a = b
        for y in range(26):
            if a > 25:
                a = 0
            chart[x][y] = alphabet[a]
            a+=1
        b+=1
    
    return chart



def cipher(plain_text=""):
    
    if not plain_text:
        return False

    # Creating strings for uppercase and lowercause alphabets, along 
    # with uppercase and lowercase Vigenere charts
    LOWER_AB = "abcdefghijklmnopqrstuvwxyz"
    UPPER_AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER_CHART = chartSetter(LOWER_AB)
    UPPER_CHART = chartSetter(UPPER_AB)

    cipher_text = ""
    index = 0

    # A list of keywords to cycle through randomly for every message that is ciphered
    keyword_list = ["key", "code", "word", "pythn", "quack"]
    index = int(random.randrange(0, 5))
    key_word = keyword_list[index]
    
    # The variable "y" is used to cycle through the letters of key_word
    y = 0
    for x in plain_text:
        if y >= len(key_word):
            y = 0
        # If the character in plain_text is not a letter or number, it is simply appended to cipher_text
        if x == " " or not (x.isalnum()):
            cipher_text += x 
        
        # Using the index of the current letter of plain_text and of key_word,
        # a row and column can be accessed in the 2D array (Vigenere chart)
        if x in LOWER_AB:
            cipher_text += LOWER_CHART[LOWER_AB.index(key_word[y])][LOWER_AB.index(x)] 
        elif x in UPPER_AB:
            cipher_text += UPPER_CHART[UPPER_AB.index(key_word[y].upper())][UPPER_AB.index(x)]
        else:
            continue
        y+=1

    # Returns a tuple of the cipher text and the index of the key_word used (from the list) 
    return (cipher_text, index)

# Deciphers the inputted message
def decipher(cipher_package):
    if not cipher_package[0]:
        return False

    keyword_list = ["key", "code", "word", "pythn", "quack"]

    index = cipher_package[1]

    cipher_text = cipher_package[0] # used for COLUMN access
    key_word = keyword_list[index] # used for ROW access

    LOWER_AB = "abcdefghijklmnopqrstuvwxyz"
    UPPER_AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER_CHART = chartSetter(LOWER_AB)
    UPPER_CHART = chartSetter(UPPER_AB)
    
    plain_text = ""

    y = 0
    temp = ""
    for x in cipher_text:
        if y >= len(key_word):
            y = 0
        if x == " " or not (x.isalnum()):
            plain_text += x
        
        # For deciphering, the row with the current letter of key_word will be accessed,
        # and the index of the column in which the current letter of cipher_text is found
        # will be accessed. Using that index, the plaintext letter will be found in the 
        # lowercase or uppercase alphabet strings 

        if x in LOWER_AB:
            plain_text += LOWER_AB[LOWER_CHART[LOWER_AB.index(key_word[y])].index(x)]
        elif x in UPPER_AB:
            plain_text += UPPER_AB[UPPER_CHART[UPPER_AB.index(key_word[y].upper())].index(x)]
        else:
            continue
        y+=1

    return plain_text
