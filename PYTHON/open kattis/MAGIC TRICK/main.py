word=input()
frequency={}
guess=0
for letter in word:
    if letter in frequency:
        frequency[letter]+=1
    else:
        frequency[letter]=1
for letter in frequency:
    if frequency[letter] > 1:
         guess+=1
    else:
        guess+0

if guess>0:
    print(0)
elif guess==0:
    print(1)


        
        
