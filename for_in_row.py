''' Four-in-a-row , of nickname:Quyetsk
 Một trò chơi tên four-in-a-row
 Gmail: quyetzz12d@gmail.com'''
import sys

# Hằng số được sử dụng để hiển thị bảng
 
EMPTY_SPACE = "."

PLAYER_X = "X"

PLAYER_0 = "0"

BOARD_WIDTH = 7

BOARD_HEIGHT = 6

COLUMN_LABELS = ("1","2","3","4","5","6","7")

assert len(COLUMN_LABELS) == BOARD_WIDTH

BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""

def main():

    ''' Chaỵ trò chơi for_in_row'''

    print("FOW-IN-ROW")

    print(''' Hai người chơi lần lượt  thả các ô vào một trong bảng cột , cố gắng tạo bốn trong một hàng
    theo chiều ngang, chiều dọc, đường chèo''')
    # Thiết lạp một trò chơi mới:

    gameBoard = getNewBoard()
    playerTurn = PLAYER_X
    while True:
        # Hiển thị bảng và nhận nước đi của người chơi
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        #ktra thăng hoặc hòa
        if isWiner(playerTurn,gameBoard):
            displayBoard(gameBoard) # hiển thị bàn cờ
            print(f" Người chơi đã thắng {playerTurn}")
            sys.exit () # beak cũng được

        elif isFull(gameBoard):
            displayBoard(gameBoard)  # hiển thị bàn cờ
            print("Kết quả hòa !")
            sys.exit()

        # chuyển lượt chơi
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_0

        elif playerTurn == PLAYER_0:
            playerTurn = PLAYER_X

def getNewBoard():
    ''' Trả về từ điển đại diện cho bảng game for in row.
     Các khóa là bộ giá trị (cột , hàng) của 2 số nguyên và
     cac giá trị là một trong các "X", "O" hoặc khoảng trống "_"
    '''
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex,rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    ''' Hiển thị bảng và các ô của nó trên màn hình
     # Chuẩn bị 1 danh schs để định dạng chuỗi cho bảng
     # Danh sách chứa tất cả các ô của bảng và khoảng trắng từ trái san g phải
     từ trên xuống dưới
     '''
    tilechars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tilechars.append(board[(columnIndex,rowIndex)])
    print(BOARD_TEMPLATE.format(*tilechars))

def getPlayerMove(playerTile,board ):
    ''' Cho phép ngưới chơi chọn một cột
    trên bảng để thả một viên vào
    Trả về một bộ (Cột , hàng) mà ô xếp vào
    '''
    # tiếp tục hỏi người chơi cho đến khi họ đi một nước đi hợp lệ
    while True:
        print(f"player{playerTile,{BOARD_WIDTH}} or 'QUIT':")
        respone = input(">> ").upper().strip()
        if respone == 'QUIT':
            print('Cam on ban da choi')
            sys.exit()
        if respone not in (COLUMN_LABELS):
            print(f" Nhập 1 số từ 1 đến {BOARD_WIDTH}")
            continue

        columnIndex = int(respone) - 1
        # cho các chỉ mục dụa trên 0
        # Nếu cột đã đầy yêu cầu di chuyển sang hướng khác
        if board[(columnIndex,0)] != EMPTY_SPACE:
            print(" Cột đã đầy hãy chọn một cột khác")
            continue

        # Trường hợp cột vẫn còn không gian trống
        # Bắt đầu từ phía dưới , tìm khoảng trống đầu tiên
        for rowIndex in range(BOARD_HEIGHT-1,-1,-1):
            if board[(columnIndex,rowIndex)] == EMPTY_SPACE:
                return (columnIndex,rowIndex)

# trường hợp kết thúc tỷ số hòa
def isFull(board):
    ''' Trả về True nếu bảng ko có khoảng trắng nước lai
    là False
    '''
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False
    return True

def isWiner(playerTile,board):
    ''' Trả về True nếu playerTile có 4 ô liên tiêp trên bngr , ngược
    lại về False
    '''
    # Xem qua toàn bộ bngr , kiểm tr xem có 4 ô trên một row
    for columnIndex in range(BOARD_WIDTH-3):
        for rowIndex in range(BOARD_HEIGHT):
            tile1= board[(columnIndex, rowIndex)]
            tile2= board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    # hang doc
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT-3):
            tile1= board[(columnIndex, rowIndex)]
            tile2= board[(columnIndex , rowIndex + 1)]
            tile3 = board[(columnIndex , rowIndex + 2)]
            tile4 = board[(columnIndex , rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    # cheo
    for columnIndex in range(BOARD_WIDTH-3):
        for rowIndex in range(BOARD_HEIGHT-3):
            tile1= board[(columnIndex, rowIndex)]
            tile2= board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex , rowIndex + 3)]

        return False
# khai bao ham main ()
if __name__ == "__main__":
    main()










