from pygame import Rect, draw

from data import Colors,\
    colToFile, rowToRank,\
    boardWhite, boardBlack, getPieceImage, sqSize


class Board:
    def __init__(self, player='white'):
        self.colors = (Colors.board1, Colors.board2)

        self.board = getBoard(board=boardWhite if player == 'white' else boardBlack if player == 'black' else boardWhite)

    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                draw.rect(screen, color, Rect(col * sqSize,
                                              row * sqSize,
                                              sqSize,
                                              sqSize))

    def drawPieces(self, screen):
        for row in self.board:
            for piece in row:
                if piece is None:
                    continue

                piece.draw(screen)


def createBoard(player='white'):
    return Board(player=player)


def getBoard(board):
    return [[Piece(color=name[0], type_=name[1], row=na, col=nb) if name is not None else None
             for nb, name in enumerate(row)] for na, row in enumerate(board)]


class Piece:
    def __init__(self, color, type_, row, col):
        self.color = color
        self.type = type_
        self.name = f'{self.color}{self.type}'
        self.image = getPieceImage(self.name)

        self.row = row
        self.col = col
        self.rank = rowToRank(self.row)
        self.file = colToFile(self.col)

    def draw(self, screen):
        screen.blit(self.image, Rect(self.col * sqSize,
                                     self.row * sqSize,
                                     sqSize,
                                     sqSize))


class Move:
    pass
