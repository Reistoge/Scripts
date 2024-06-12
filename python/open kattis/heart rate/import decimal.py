import decimal
number=int(input())
dec = decimal.Decimal ('60') # create a Decimal object from a string
format(number,".3f")
s = format (dec, '.4f') # format the Decimal object to a fixed point notation with 3 digits after the decimal point
print (s) # print the formatted string
