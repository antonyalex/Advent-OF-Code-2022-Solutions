with open ('input.txt','r') as f:
    a=f.read().split('\n')
    
def part1():  
    s=0
    score={"X":1,"Y":2,"Z":3}
    draw={"A":"X","B":"Y","C":"Z"}
    for i in a:
        if i[2]==draw[i[0]]:
    
            s=s+score[i[2]]+3
        
        elif (i[0]=="A" and i[2]=="Y") or (i[0]=="B" and i[2]=="Z") or (i[0]=="C" and i[2]=="X"):
            s=s+score[i[2]]+6
        
        else:
            s=s+score[i[2]]
        
    print(s)
def part2():
    s=0
    score={"A":1,"B":2,"C":3}
    win={"A":"B","B":"C","C":"A"}
    loss={"A":"C","B":"A","C":"B"}
    for i in a:
        if i[2]=="Y":
            move=i[0]
            s=s+score[move]+3
        elif i[2]=="Z":
            move=win[i[0]]
            s=s+score[move]+6
        elif i[2]=="X":
            move=loss[i[0]]
            s=s+score[move]
    print(s)
part2()

            



