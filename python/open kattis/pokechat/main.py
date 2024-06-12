encoding = input()
msg = input()

for i in range(0, len(msg), 3):
    
    print(int(msg[i:i+3]))
    print(encoding[int(msg[i:i+3])-1], end="")
    
