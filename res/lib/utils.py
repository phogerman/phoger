#This library is for the utility functions which may be globally needed
import json


#########################################
#Function to convert dictionary to binary
 
def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)

    #Add 0's to make every element with exactly 8 bits

    x = binary.split(" ")
    abc = []
    for items in x:
        item = items.zfill(8)
        abc.append(item)
    result = " ".join(abc)

    #Strip all the spaces in the binary

    bin_wo_spaces = result.replace(" ", "")
    return bin_wo_spaces

#Function to convert binary to dictionary

def binary_to_dict(the_binary):
    #Add space after 8 bits in the binary
    bin_val = add_spaces(the_binary)

    jsn = ''.join(chr(int(x, 2)) for x in bin_val.split())
    d = json.loads(jsn)  

    return d

#Funtion to add spaces after specified length throughout the string

def add_spaces(string):
    n = 8	# every 8 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    return " ".join(split_string)


#########################################