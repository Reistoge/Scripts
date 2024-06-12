def Introducción():
    print("Hola")

a = "Palabra"
print(id(a))
## takes one argument and returns that object’s unique integer identifier
##-------------------------------------------------------------------------##
## LEN FUNCTION
print(len(a))
## 7 letter has the word Palabra
## len() returns the length of the argument passed to it
z =[a, "hola", 7, 1.5]
print(len(z))
# in this case the list z has 4 elements so the lens is 4 
##--------------------------------------------------------------------------##
## ANY FUNCTION
##any() takes an iterable as its argument and returns True if any of the items in the iterable are truthy and False otherwise
print(any([3+2==6, len("Fer")==5, 1+1==2]))

