
import sys
def index_of_empty(board, i, j):
    for x in range(i,9):
            for y in range(j,9):
                    if board[x][y] == 0:
                            return x,y
    for x in range(0,9):
            for y in range(0,9):
                    if int(board[x][y]) == 0:
                        return x,y
    return -1,-1

def satisfy_constraint(board, i, j, var):
    flagRow= all([var != board[i][x] for x in range(9)])
   
    if flagRow:
        flag_col=flag= all([var != board[x][j] for x in range(9)])
         
        if flag_col:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                    xbox, ybox =i - i % 3, j - j % 3
                    for x in range(0, 3):
                            for y in range(0, 3):
                                   
                                    if board[x+xbox][y+ybox] == var:
                                          
                                            return False
                    return True
    return False
def found_in_Row(board,var,row):
    
   flag= all([var != board[row][x] for x in range(9)])
   if(flag) :            
    return True
   else:
       return False 
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
                
       
        
def found_in_coluumn(board,var,col):
    for x in range(9):
        if board[x][col]==var:
            return False
    
    return True        
def backtracking(board, domain,i=0, j=0,):
    i,j = index_of_empty(board, i, j)
    if i == -1:
            return True,board
    for e in domain:
            if satisfy_constraint(board,i,j,e):
                    board[i][j] = e
                    flag,board=backtracking(board,domain ,i, j)
                    if flag:
                            return True,board
                        # undo  for backtracking
                    board[i][j] = 0
    return False,board


def read():
    
    lines=[]   
    
    ins=open('data.txt')
    for i in ins :
        
        lines.append(i)
       
    board=[]
    for i in range(len(lines)):
        x=lines[i]
        small=[]
        for sympole in x :
            if sympole!=',' and sympole!='[' and  sympole!=']' and  sympole!='\n':
                num=int(sympole)
               
                small.append(num)
        board.append(small)            
        
   

    return board

if __name__ == '__main__':
    
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    input= read()
       
       
    flag,sudak=backtracking(input, domain, i=0, j=0)
   
    print_result(sudak)
    
