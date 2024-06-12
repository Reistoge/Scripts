# dar vuelta string
# encontrar el indice de una palabra
def find_index(string, letra):
    for i in range(0,len(string),1):
        if string[i]==letra:
            return i
    return ValueError


def Permute(string,  letra1,  letra2):
    new_str=""
    b=find_index(string, letra1)
    c=find_index(string, letra2)
    for i in range(0,len(string),1):
        if i!=c and i!=b:
            new_str+=string[i]
        elif i==c:
            new_str+=string[b]
        elif i==b:
            new_str+=string[c]
    return new_str

print(Permute("hola","h","l"))
            


    


