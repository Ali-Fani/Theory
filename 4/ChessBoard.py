x, y = [int(s) for s in str(
    input("Enter Two Numbers (Seprate with space) : ")).split(' ')]
board = [["□"] * y for i in range(x)]
for i in range(x):
    for j in range(y):
        if i % 2 == 0 and j % 2 == 0:
            board[i][j] = "■"
        elif i % 2 == 1 and j % 2 == 1:
            board[i][j] = "■"


for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=" ")
    print()
