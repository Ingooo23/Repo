def shift_letter(letter, shift):
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterinletters = x.find(letter)

    finalshift = shift + letterinletters -26*int((shift+letterinletters)/26)

    if letter.isalpha() == False:
        finalletter = " "
    else: 
        finalletter = x[finalshift]

    return finalletter


def caesar_cipher(message, shift):
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lettercount = len(message) - 1
    l = 0

    new_message = ""
    while l <= lettercount:
        current_letter = message[l]

        finalshift = shift + x.find(current_letter) - 26*int((shift+x.find(current_letter))/26)
        
        if current_letter == " ":
            new = " "
            new_message = new_message + new
        else:
            new_letter = x[finalshift]
            new = message[l].replace(message[l],new_letter, -1)
            new_message = new_message + new
        l = l+1
    return new_message


def shift_by_letter(letter, letter_shift):
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = x.find(letter_shift)
    z = x.find(letter)
    finalshift = y + z - 26*int((y+z)/25)
    if letter.isalpha() == False:
        new_letter = " "
    else:
        new_letter = x[finalshift]
    return new_letter


def vigenere_cipher(message, key):
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keycount = len(key) - 1
    messagecount = len(message) - 1

    k = 0
    l = 0

    new_message = ""

    while l <= messagecount:
        shift = ""

        if k > keycount:
            k = 0

        key_current = key[k]
        keylettervalue = x.find(key_current)
        message_current = message[l]
        messagelettervalue = x.find(message_current)
        shift = keylettervalue + messagelettervalue - 26*int((keylettervalue + messagelettervalue)/25)
        new = x[shift]
        if key_current.isalpha() == False:
            new = " "
        if message_current.isalpha() == False:
            new = " "
        new_message = new_message + new

    
        l = l+1
        k = k+1
    return new_message


def scytale_cipher(message, shift):
    i = 0
    x = 0
    shifted_message = ""
    mult = len(message)%shift
    if mult != 0:
        while x < 10:
            message = message + "_"
            if len(message)%shift == 0:
                x = 10
    newshift = int(len(message)/shift)
    for i in range(0, len(message)):
            finalshift = i*newshift - len(message)*int((i*newshift)/len(message)) + int(i/shift)
            shifted_message = shifted_message + message[finalshift]
    return shifted_message

def scytale_decipher(message, shift):
    shifted_message = ""
    for i in range(0, len(message)):
        final_shift = shift*i - len(message)*int((i*shift)/len(message)) + int((i*shift)/len(message))
        shifted_message = shifted_message + message[final_shift]
    return shifted_message
