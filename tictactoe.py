
board = ['-','-','-','-','-','-','-','-','-']

def drawBoard():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])
    

 
    
drawBoard()

print("X always goes first")

turn = str('X')


        
        
try:           

while True:
    
    print("player " + turn + " put in number between 0 and 8")
    placeSelection = int(input())

    if board[placeSelection] == '-':
        board[placeSelection] = turn
    else:
        print("this place is taken")
        drawBoard()
        continue

    drawBoard()
    #check for win
    if (board[0] == turn and board[1] == turn and board[2] == turn or 
        board[3] == turn and board[4] == turn and board[5] == turn or
        board[6] == turn and board[7] == turn and board[8] == turn or
        board[0] == turn and board[4] == turn and board[8] == turn or
        board[2] == turn and board[4] == turn and board[6] == turn or
        board[0] == turn and board[3] == turn and board[6] == turn or
        board[1] == turn and board[4] == turn and board[7] == turn or
        board[2] == turn and board[5] == turn and board[8] == turn):
            print("Player " + turn + " wins")
            break
    #check for draw
    a = 0  
    for i in board:
        if i == '':
            a = a + 1
    if a == 0:
        print("draw")
        break
    #alternate turns
    if turn == str('X'):
        turn = str('O')
    else:
        turn = str('X')
    continue

print("end of game")

except:
print("error!")