with open ('input.txt','r') as f:
    a=[i.split(',') for i in f.readlines()]
    a=[[i[0],i[1].strip()] for i in a]
    print(a)
    c1=0
    c2=0
    for i in a:
        l1=[]
        l2=[]
        b=i[0].split('-')
        for j in range(int(b[0]),int(b[1])+1):
            l1.append(str(j))
        c=i[1].split('-')
        for k in range(int(c[0]),int(c[1])+1):
            l2.append(str(k))
        if all(x in l1 for x in l2) or all(x in l2 for x in l1):
            c1+=1
       
        if any(x in l1 for x in l2) or any(x in l2 for x in l1):
            c2+=1
    print(c2)

    

        

  
    

  
  
    


        
