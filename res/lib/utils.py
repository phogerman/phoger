#This library is for the utility functions which may be globally needed


#Function to convert binary to string

def bin_to_str(bin_data):
    
    def BinaryToDecimal(binary):
        string = int(binary, 2)
        return string

    str_data =' '

    for i in range(0, len(bin_data), 7):

        temp_data = bin_data[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)

    return str_data
 
