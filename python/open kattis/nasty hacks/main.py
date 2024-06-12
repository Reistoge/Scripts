N=int(input())
test_cases=[]

for i in range(0,N,1):
    numbers=input()
    numbers=numbers.split()
    for number in numbers:
        r=int(numbers[0])
        e=int(numbers[1])
        c=int(numbers[2])
        
    
    if r==(e-c):
        test_cases.append("does not matter")
    elif r<(e-c):
        test_cases.append("advertise")
    elif r>(e-c):
        test_cases.append("do not advertise")

for case in test_cases:
    print(case)



    

    
