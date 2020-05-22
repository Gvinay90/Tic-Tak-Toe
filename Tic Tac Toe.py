def game_board(board):
    print(board[6],"|",board[7],"|",board[8])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[0],"|",board[1],"|",board[2])
def desk1(board,win,count):
    game_board(board)
    a=int(input("Player1 turn\n"))
    if board[a-1]!="X" and board[a-1]!="O":
        board[a-1]="X"
        count-=1
    else:
        print("Invalid Move!!")
        print("Try Again!!")
        return desk1(board,win,count)
    for i in win:
        if board[i[0]]==board[i[1]]==board[i[2]]=="X":
            print("Player1 wins")
            return game_board(board)
    if count==0:
        return replay()
    return desk2(board,win,count)
def desk2(board,win,count):
    game_board(board)
    a=int(input("Player2 turn\n"))
    if board[a-1]!="X" and board[a-1]!="O":
        board[a-1]="O"
        count-=1
    else:
        print("Invalid Move!!")
        print("Try Again!!")
        return desk2(board,win,count)
    for i in win:
        if board[i[0]]==board[i[1]]==board[i[2]]=="O":
            print("Player2 wins")
            return game_board(board)
    if count==0:
        return replay()
    return desk1(board,win,count)
def replay():
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    board=[" "," "," "," "," "," "," "," "," "]
    count=9
    return desk1(board,win,count)
replay()
