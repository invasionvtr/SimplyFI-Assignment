Write a python code for converting integer values to Indian currency notations, without using the currency libraries.

def int_to_inr():
  
    num = int(input("Enter an integer value: "))
    num_str = str(num)  # Convert the integer to a string
    n = len(num_str)
    if n <= 3:  # If the number has less than or equal to 3 digits
        return num_str  # Return the string as it is
    else:
      
        comma_pos = n % 2  
        inr_str = num_str[:comma_pos]
        while comma_pos < n:
            inr_str += ',' + num_str[comma_pos:comma_pos+2]
            comma_pos += 2
        return inr_str

print(int_to_inr())
