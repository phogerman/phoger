# This Library consists of Symmetric key algorithms to be used for encrypting our data
# This library will be used inside the file 'phoger.py'

from Crypto.Cipher import AES
from . import utils
from base64 import b64encode
from base64 import b64decode
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
    
    ##############################################################
    #Here we are going to return the binary representation 
    #of the json dictionary which will be converted back to the 
    #dictionary form by the decrypt function
    ##############################################################
    return utils.dict_to_binary(result)
    


def decrypt_AES_256_gcm(encrypted_msg,key):
    #Stating JSON Components
    b64 = json.loads(utils.binary_to_dict(encrypted_msg))
    json_k = [ 'nonce', 'ciphertext', 'tag' ]
    jv = {k:b64decode(b64[k]) for k in json_k}

    #Decrypting with the components
    
    aesCipher = AES.new(key.encode('utf8'), AES.MODE_GCM, jv['nonce'])
    plaintext = aesCipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
    #return plaintext   
    
    
    #####################################################
    # Here we return the plaintext
    #####################################################
    
    return plaintext
