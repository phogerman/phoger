#For Encryption
from res.lib import enclib

#Basic utility
from res.lib import utils
import hashlib,json

# For Pillow
from PIL  import Image

#For Arguments parsing
import argparse



# Parsing the arguments from command line

parser = argparse.ArgumentParser(description="Phoger Image Steganography App")
parser.add_argument('msg', metavar='msg',
                    type=str, help='Message to encrypt.')
parser.add_argument('password', metavar='password',
                    type=str, help='Password for encrypting.')
args = parser.parse_args()
password = args.password
msg = args.msg

# Function to Convert the given password to 32 byte MD5 Hash


def to_md5(password):
    pass_in_md5 = hashlib.md5(password.encode())
    pass_hash = pass_in_md5.hexdigest()
    return pass_hash


# Function to encrypt to AES 256 GCM ,a bit string will be returned
encrypted_msg = enclib.encrypt_AES_256_GCM(msg, to_md5(password))

# The length of the string is attached to the beginning 32 bits of the string
msg_to_encode = '{:032b}'.format(len(encrypted_msg)) + encrypted_msg + '00000000'

# Pillow Integration

##################################################
#Encoding to image
##################################################

im = Image.open('src.png')
img = im.load()
print(im.size)
[xs,ys] = im.size

# Checking if the image size is enough to write the message
len_msg = len(msg_to_encode) - 8

if(xs*ys*4 >= len_msg):
    #Encode the message to image
    k = 0 #index for msg
    while(k <= len_msg):
        for i in range(ys):
            for j in range(xs):
                (r,g,b,a) = img[j,i]
                # k th
                if(msg_to_encode[k] == 0):
                    if(r%2 == 1):
                        r -= 1
                else:
                    if(r%2 == 0):
                        r += 1
                # k+1 th
                if(msg_to_encode[k+1] == 0):
                    if(g%2 == 1):
                        g -= 1
                else:
                    if(g%2 == 0):
                        g += 1        
                # k+2 th
                if(msg_to_encode[k+2] == 0):
                    if(b%2 == 1):
                        b -= 1
                else:
                    if(b%2 == 0):
                        b += 1       
                # k+3 th         
                if(msg_to_encode[k+3] == 0):
                    if(a%2 == 1):
                        a -= 1
                else:
                    if(a%2 == 0):
                        a += 1
                img[j,i] = (r,g,b,a)
                k += 4        
                if(k >len_msg):
                    break
            if(k>len_msg):
                break        


#width*height
else:
    print("[-] The resoulution is not enough")  

"""
# Examine every pixel in im
for x in range(0,xs):
    for y in range(0,ys):
        #get the RGB color of the pixel
        img[x,y] = [r,g,b]
"""
im.save('output.png')
 
##################################################
# Decoding from image
##################################################


#######################################################################
#Test and Trial Printing section below
#######################################################################

#print("Message = ", encrypted_msg, "  Password Hash=", to_md5(password))

#print("len=",enclib.decrypt_AES_256_gcm(encrypted_msg,"abc"))
#m = to_md5("manu4")
#print(enclib.decrypt_AES_256_gcm(encrypted_msg[0],m),"\n\n\n")

#print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
print(encrypted_msg,enclib.decrypt_AES_256_gcm(encrypted_msg,to_md5(password)),msg_to_encode)

#print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))



#print(encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
