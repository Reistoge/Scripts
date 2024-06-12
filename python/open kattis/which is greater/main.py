
numbers=input()
""" split convierte tu variable en una lista el cual separa cada elemento por cada espacio que haya entre las palabras. """
numbers=numbers.split()
a=int(numbers[0])
b=int(numbers[1])
if(a<=b):
    print(0)
else:
    print(1)
