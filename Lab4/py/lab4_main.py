from PIL import Image
import numpy as np


def imgToMes(img_mess):

    # reading the picture as an array of pixels
    im = Image.open(img_mess, 'r')
    arr = np.array(im.getdata())

    # creating a message that should be encoded
    mess = ''
    for i in arr:
        for j in i:
            #getting bits starting from the 2nd one
            x = bin(j)[2::]
            if len(x) < 8:
                b = 8 - len(x)
                x = '0'*b + x
            mess += x


    # adding the size of the picture to the string
    width, height = im.size
    for i in [width,height]:
        x1 = bin(i)[2::]
        if len(x1) < 8:
            b1 = 8 - len(x1)
            x1 = '0' * b1 + x1
        mess += x1
    return mess


# encrypting a message
def encryptMes(message, path_container, path_save):

    # reading an image as an array of pixels
    img = Image.open(path_container, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))


    # checking the format of pixels
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    amount_pixels = array.size//n


    # adding the delimiter at the end of the message
    m = "$t3g0"
    mess_bits = message
    mess_bits += ''.join([format(ord(i), "08b") for i in m])


    # checking the amount of required pixels
    amount_required_pixels = len(mess_bits)
    print(amount_required_pixels)

    if amount_required_pixels > amount_pixels:
        print("The image is too small to encrypt the massage. Try using a bigger picture")
    else:
        ind=0
        j = 2

        # iterating through the pixels and adding the message to the two last bits of pixels
        for p in range(amount_pixels):
            for q in range(0, 3):
                if ind < amount_required_pixels:
                    print(bin(array[p][q])[2:9 - j + 1],mess_bits[ind:ind + j])
                    array[p][q] = int(bin(array[p][q])[2:9 - j + 1] + mess_bits[ind:ind + j], 2)
                    # print("Changed bits: " + str(bin(array[p][q])))
                    ind += j


        # saving the array of pixels as an image
        array = array.reshape(height, width, n)
        #  print(array)
        img_encrypted = Image.fromarray(array.astype('uint8'), img.mode)
        img_encrypted.save(path_save)
        print("The message has been encrypted successfully")


# Decrypting the message
def decryptMes(path_container):

    # reading an image as an array of pixels
    img = Image.open(path_container, 'r')
    array = np.array(list(img.getdata()))


    # checking the format of pixels
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    amount_pixels = array.size//n


    # iterating through each pixel, converting it to bits and reading the last two bits
    mess_bits = ""
    k=2
    for p in range(amount_pixels):
        for q in range(0, 3):
            a = bin(array[p][q])[2:]
            # print(a[len(a)-k:len(a)])
            mess_bits += (a[len(a)-k:len(a)])


    # slicing the string of bits on groups of 8 bit strings
    mess_bits = [mess_bits[i:i+8] for i in range(0, len(mess_bits), 8)]
    # print(mess_bits)


    # converting each hiden bit to an int and a char
    message = ""
    mess_ints = []
    for i in range(len(mess_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(mess_bits[i], 2))
            mess_ints.append(int(mess_bits[i], 2))
   # print(mess_ints)


    # getting the size of the picture from the array
    width = mess_ints[-7]
    height = mess_ints[-6]
    mess_ints = mess_ints[:-7]


    # checking if the delimiter is found
    if "$t3g0" in message:
        print("Hidden Message:")
    else:
        print("No Hidden Message Found")


    # converting the message to a 2D array of integers and saving it as a bmp file
    mess_ints = [[mess_ints[i],mess_ints[i+1],mess_ints[i+2]] for i in range(0,len(mess_ints),3)]
    arr = np.array(mess_ints)
    arr = arr.reshape(height, width, 3)
    print(arr)
    dec = Image.fromarray(arr.astype('uint8'), 'RGB')
    dec.save('../files/message_recreated.bmp')



# main___________________________________________
img_message = '../files/message.bmp'
mes = imgToMes(img_message)
print(f'The length of the message: {len(mes)}')

img_container = '../files/flower.bmp'
img_encrypted = '../files/message_encrypted.bmp'

encryptMes(mes, img_container, img_encrypted)
decryptMes(img_encrypted)