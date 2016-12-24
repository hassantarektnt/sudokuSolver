
import sys

import copy


def propagate( x,y,val, constraints,board):
    key=constraints.keys()
   
    
    for z in key:       
        a,b=z
        if (a==x or b==y )and (board[a][b]==0):
        
            if val in constraints[z]:    
                    constraints[z].remove(val)
         
        for i in range(0,3):
            for j in range(0,3):
                xbox=x-x%3
                ybox= y-y%3
                if(xbox+i==a and ybox+j==b)and (board[a][b]==0):
                    if val in constraints[z]:
                        constraints[z].remove(val)
                   
def fwd_checking(index,arr, assignment, constraints, board):
   
    if len(arr)==index:
        return True,board
     
    x,y=arr[index]
   
    
    nw_constraints = copy.deepcopy(constraints)
    for val in range (1,10):
        #constraints[(x,y)]:
       
        nw_assignment = assignment.copy()
        nw_assignment[(x,y)] = val

        if satisfy_constraint(board, x, y, val):
           
            board[x][y]=val
           
            propagate(x,y ,val, nw_constraints,board)
          
        
             
            result,second = fwd_checking(index+1,arr, nw_assignment, nw_constraints, board)
            if result==True: 
                return result,second
            board[x][y] = 0 
    return False,board
        
import copy

 
       
        
def satisfy_constraint(board, i, j, var):
    flagRow= all([var != board[i][x] for x in range(9)])
   
    if flagRow:
        flag_col=flag= all([var != board[x][j] for x in range(9)])
         
        if flag_col:                       
                    xindex, yindex =i - i % 3, j - j % 3
                    for x in range(0, 3):
                            for y in range(0, 3):
                                   
                                    if board[x+xindex][y+yindex] == var:
                                            
                                            
                                            return False
                    return True
   
    return False       
 
def get_emptyplace(board):
     
       
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    emptyCells.append((i, j))
       
                    
        return emptyCells
                    
def Suduko(board):
    assignment={}
    emptyplace=[]
    list1=[]
    constraints={}
    
#     print (board)
    nwboard=copy.deepcopy(board)   
   
    
    emptyplace=get_emptyplace(board) 
   
    for e in emptyplace:
       
            list1=[z for z in range(1,10 )]
            
            constraints[e]=list1
          
   
    result,w = fwd_checking(0,emptyplace, assignment, constraints, board)
 
    return False, w

def display(a):
    sys.stdout.write(str(a))   
    
def print_result(board):
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == 0 or isinstance(cell, set):
                display('.')
            else:
                display(cell)
            if (j + 1) % 3 == 0 and j < 8:
                display(' |')

            if j != 8:
                display(' ')
        display('\n')        
        display("- - - - - - - - - - -\n") 
 
def read():
    
    lines=[]   
    
    ins=open('data.txt')
    for i in ins :
        
        lines.append(i)
       
    board=[]
    for i in range(len(lines)):
        x=lines[i]
        small=[]
        for simple in x :
            if simple!=',' and simple!='[' and  simple!=']' and  simple!='\n':
                num=int(simple)
               
                small.append(num)
        board.append(small)            
        


    return board

if __name__ == '__main__':
    
    input= read()

    flag,sudak=Suduko(input)
  
    print_result(sudak)
      

    
    
