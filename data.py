from pygame import Color, image, time, transform


boardWidth = 512
boardHeight = 512
sqSize = min(boardWidth, boardHeight) // 8


def getClock():
    return time.Clock()


class Colors:
    white = Color('white')
    grey = Color('grey')
    black = Color('black')
    red = Color('red')
    orange = Color('orange')
    yellow  = Color('yellow')
    green = Color('green')
    blue = Color('blue')
    purple = Color('purple')

    fill = white
    board1 = white
    board2 = Color(255, 204, 255)
    border = Color(50, 50, 50)

    selected = purple
    validMoves = yellow
    preMoves = red
    postMove = red


pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

boardWhite = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
              ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
              ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]

boardBlack = [['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
              ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, None],
              ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
              ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br']]


def getPieceImage(piece):
    return transform.scale(image.load(f'images/{piece}.png').convert_alpha(), (sqSize, sqSize))


def fileToCol(file):
    return int(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h').index(file) + 1)


def rankToRow(rank):
    return int(rank)


def rowToRank(row):
    return int(row)


def colToFile(col):
    return ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')[col-1]
