encoding = input()
msg = input()

for i in range(0, len(msg), 3):
    fragment = msg[i:i+3]
    index = int(fragment)-1
    print(encoding[index], end="")