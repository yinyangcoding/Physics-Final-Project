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
    LOWER_AB = "abcdefghijklmnopqrstuvwxyz"
    UPPER_AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER_CHART = chartSetter(LOWER_AB)
    UPPER_CHART = chartSetter(UPPER_AB)

    cipher_text = ""
    index = 0

    #index = int(random.randrange(0, len(keyword_list)))
    
    keyword_list = ["key", "code", "word", "pythn", "quack"]
    
    index = int(random.randrange(0, 5))
    
    key_word = keyword_list[index]


    #if not(key_word.isalnum()):
        #while not(key_word.isalnum()):
            #index = int(random.randrange(0, len(keyword_list)))
            #key_word = keyword_list[index]
    
    if len(key_word) > 5:
        key_word = key_word[:6]
    

    y = 0
    for x in plain_text:
        if y >= len(key_word):
            y = 0
        if x == " ":
            cipher_text += x 

        if x in LOWER_AB:
            cipher_text += LOWER_CHART[LOWER_AB.index(key_word[y])][LOWER_AB.index(x)] 
        elif x in UPPER_AB:
            cipher_text += UPPER_CHART[UPPER_AB.index(key_word[y].upper())][UPPER_AB.index(x)]
        else:
            continue

        y+=1

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
        if x == " ":
            plain_text += " "
        if x in LOWER_AB:
            plain_text += LOWER_AB[LOWER_CHART[LOWER_AB.index(key_word[y])].index(x)]
        elif x in UPPER_AB:
            plain_text += UPPER_AB[UPPER_CHART[UPPER_AB.index(key_word[y].upper())].index(x)]
        else:
            continue
        y+=1

    # General idea: iterating through each letter, access the row of the chart using each
    # character of key_word. Then, find the index of the column in which the current 
    # cipher_text letter exists. Using that index, trace the plain text letter used, and
    # append that to the string plain_text


    return plain_text



print(cipher("Matt is a cutie"))

print(decipher(cipher("Matt is a cutie")))