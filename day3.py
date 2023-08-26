with open ('input.txt','r') as f:
    a=[a.strip() for a in f.readlines()]
    
def priority_value_sum(common_chars):
    priority_values=[]
    for i in common_chars:
        if i.islower():
            priority_value=ord(i)-96
        else:
            priority_value=ord(i)-38
        priority_values.append(priority_value) 
    return(sum(priority_values))

def part1():
    b=[]
    for i in a:
        b.append([i[0:len(i)//2],i[len(i)//2:]])
    common_chars=[]
    for j in b:
        common_char=''.join(set(j[0]).intersection(set(j[1])))
        common_chars.append(common_char)
    print(priority_value_sum(common_chars))

def part2():
    common_chars=[]
    for i in range(0,len(a),3):
        common_char=''.join(set(a[i]).intersection(set(a[i+1]).intersection(set(a[i+2]))))
        common_chars.append(common_char)
    print(common_chars)
    print(priority_value_sum(common_chars))

part2()
