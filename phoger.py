from res.lib import enclib
import argparse
import hashlib


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


#######################################################################
#Test and Trial Printing section below
#######################################################################

#print("Message = ", encrypted_msg, "  Password Hash=", to_md5(password))

#print("len=",enclib.decrypt_AES_256_gcm(encrypted_msg,"abc"))

#print(enclib.decrypt_AES_256_gcm(encrypted_msg[0],m),"\n\n\n")
<<<<<<< HEAD
print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
#print(encrypted_msg)
=======
#print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
print(encrypted_msg)
>>>>>>> 0aebe5788efd0b95a4f7542ee961900a975fab7e
