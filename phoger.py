#For Encryption
from res.lib import enclib

#Basic utility
from res.lib import utils
import hashlib,json

#For Pillow
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
msg_to_encode = '{:032b}'.format(len(encrypted_msg)) + encrypted_msg


# Pillow integration
im=Image.open('src.png')
img=im.load()
print(im.size)
[xs,ys]=im.size

# Checking if the image size is enough to write the message
if(xs*ys >= len(msg_to_encode)):
    #Encode the message to image




  #width*height

"""
# Examine every pixel in im
  for x in range(0,xs):
     for y in range(0,ys):
        #get the RGB color of the pixel
        img[x,y] = [r,g,b]
"""
im.save('output.png')
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
