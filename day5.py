with open ("input.txt",'r') as f:
    a=[]
    stacks=['','','','','','','','','']
    for i in range(0,8):
        l=f.readline().replace('    ',"[@]").replace(' ','').replace('[','').replace(']','').rstrip()
        a.append(l)
    a=list(reversed(a))
    a=[list(i) for i in a]
    
    for i in a:
        for j in range(0,len(i)):
            stacks[j]=stacks[j]+i[j]
    stacks_init=[list(i) for i in stacks]
    stacks_final=[]
    for m in stacks_init:
        a=[i for i in m if i!="@"]
        stacks_final.append(a)
        


    f.readline()
    moves=[i.rstrip().split() for i in f.readlines()]
    for k in moves: 
        popped_values=[]
        for j in range(0,int(k[1])):
            popped_value=stacks_final[int(k[3])-1].pop()
            popped_values.append(popped_value)
        stacks_final[int(k[5])-1].extend(list(reversed(popped_values)))
    print(stacks_final)
    s=''.join([i[-1] for i in stacks_final])
    print(s)


            
 

    
      

