# This Library consists of Symmetric key algorithms to be used for encrypting our data
# This library will be used inside the file 'phoger.py'

from Crypto.Cipher import AES
from . import utils
from base64 import b64encode
import json

# AES 256 GCM ENCRYPTION


def encrypt_AES_256_GCM(msg, key):
    key_hex = key.encode('utf8')
    aesCipher = AES.new(key_hex, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg.encode('utf8'))

    #Converting output to JSON
    json_k = [ 'nonce', 'ciphertext', 'tag' ]
    json_v = [ b64encode(x).decode('utf-8') for x in [aesCipher.nonce, ciphertext, authTag ]]
    result = json.dumps(dict(zip(json_k, json_v)))
    
    

    """
    #Convert Components to strings

    str_cipher = b64encode(ciphertext).decode('utf-8')
    str_nonce = b64encode(aesCipher.nonce).decode('utf-8')
    str_authTag = b64encode(authTag).decode('utf-8')


    #The data from string is converted to bits 

    bit_cipher = ''.join(format(ord(i), '08b') for i in str_cipher)
    bit_nonce = ''.join(format(ord(i), '08b') for i in str_nonce)
    bit_authTag = ''.join(format(ord(i), '08b') for i in str_authTag)

    #The length of the ciphertext is added to the start for using at the time of decryption
    length_bit_cipher = '{:032b}'.format(len(bit_cipher)) """

    """
    We are returning the concatenated string of binary representations of
        32 bit representation of length of ciphertext, 
        ciphertext,
        aesCipher.nonce,
        authTag.
    """
    #return length_bit_cipher+bit_cipher+bit_nonce+bit_authTag,bit_cipher

    
    #####################################################
    #Test code Section
    #####################################################
    #return bit_cipher
    #return length_bit_cipher+bit_cipher+bit_nonce+bit_authTag 
    #return bit_nonce
    return result
    


def decrypt_AES_256_gcm(encrypted_msg,key):
    len_of_ciphertext = encrypted_msg[0:32]
    len_ciphertext = int(len_of_ciphertext, 2)

    #Slicing the encrypted message string to 3 components

    bit_ciphertext = encrypted_msg[32:32+len_ciphertext]
    bit_nonce = encrypted_msg[32+len_ciphertext:160+len_ciphertext]
    bit_authTag = encrypted_msg[160+len_ciphertext:288+len_ciphertext] 

    #Converting components to back to string
    """
    ciphertext = bytes([int(i) for i in bit_ciphertext])
    nonce = bytes([int(i) for i in bit_nonce])
    authTag = bytes([int(i) for i in bit_authTag])

    #Decrypting with the components
    
    aesCipher = AES.new(key.encode('utf8'), AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    #return plaintext   
    
    """
    #####################################################
    #Test code Section
    #####################################################
    
    return utils.bin_to_str(bit_ciphertext)

    """
    #return len_of_ciphertext,bin_ciphertext
    return ciphertext,nonce,authTag"""
