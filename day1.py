with open('input.txt','r') as f:
    lines=[i.rstrip() for i in f.readlines()]
    sum_calories=[],sum_calories_current_elf=0
    for i in lines:
        if i!="":
            sum_calories_current_elf+=int(i)
        else:
            sum_calories.append(sum_calories_current_elf)  
            sum_calories_current_elf=0
    sum_calories=sorted(sum_calories)
    print("Part 1:"+str(sum_calories[len(sum_calories)-1]))
    print("Part 2:"+str(sum(sum_calories[len(sum_calories)-3:len(sum_calories)])))

    
    
        
