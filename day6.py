with open('input.txt','r') as f:
    a=f.read()
    char_no=0
    for i in range(0,len(a)-13):
        substring=a[i:i+14]
        if len(substring)==len(set(substring)):
            char_no=i+14
            break
    print(char_no)