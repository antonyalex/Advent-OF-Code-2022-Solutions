def part1():
    with open('input.txt','r') as f:
        matrix=[i.strip() for i in f.readlines()]
        visible_trees=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if i==0 or j==0 or i==len(matrix)-1 or j==len(matrix[i])-1:
                    visible_trees.append(matrix[i][j])
                else:
                    flag=0
                    right_values=[]
                    for k in range(j+1,len(matrix[i])):
                        right_values.append(int(matrix[i][k]))
                    if all(int(matrix[i][j])>m for m in right_values):
                        flag+=1
                    
                    left_values=[]
                    for k in range(0,j):
                        left_values.append(int(matrix[i][k]))
                    if all(int(matrix[i][j])>m for m in left_values):
                        flag+=1
                
                    down_values=[]
                    for k in range(i+1,len(matrix)):
                        down_values.append(int(matrix[k][j]))
                    if all(int(matrix[i][j])>m for m in down_values):
                        flag+=1
                    
                    up_values=[]
                    for k in range(0,i):
                        up_values.append(int(matrix[k][j]))
                    if all(int(matrix[i][j])>m for m in up_values):
                        flag+=1
                    if flag>=1:
                        visible_trees.append(matrix[i][j])
        print(len(visible_trees))

def part2():
    with open('input.txt','r') as f:
        matrix=[i.strip() for i in f.readlines()]
        scenic_scores=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                scenic_score=1
                right_values=[]
                for k in range(j+1,len(matrix[i])):
                    right_values.append(int(matrix[i][k]))
                c1=0
                for value in right_values:
                    if value<int(matrix[i][j]):
                        c1+=1
                    elif value>=int(matrix[i][j]):
                        c1+=1
                        break
                    else:
                        break
                scenic_score=scenic_score*c1

                
                
                left_values=[]
                for k in range(0,j):
                    left_values.append(int(matrix[i][k]))
                c2=0
                left_values=list(reversed(left_values))
                for value in left_values:
                    if value<int(matrix[i][j]):
                        c2+=1
                    elif value>=int(matrix[i][j]):
                        c2+=1
                        break
                    else:
                        break
                scenic_score=scenic_score*c2
                
                down_values=[]
                for k in range(i+1,len(matrix)):
                    down_values.append(int(matrix[k][j]))
                c3=0
                for value in down_values:
                    if value<int(matrix[i][j]):
                        c3+=1
                    elif value>=int(matrix[i][j]):
                        c3+=1
                        break
                    else:
                        break
                scenic_score=scenic_score*c3

                
                up_values=[]
                for k in range(0,i):
                    up_values.append(int(matrix[k][j]))
                up_values=list(reversed(up_values))
                c4=0
                for value in up_values:
                    if value<int(matrix[i][j]):
                        c4+=1
                    elif value>=int(matrix[i][j]):
                        c4+=1
                        break
                    else:
                        break
                scenic_score=scenic_score*c4
                

                scenic_scores.append(scenic_score)
        print(max(scenic_scores))
                
                





part2()



                    
                    
                
                    
    
              