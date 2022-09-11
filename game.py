from chess import createBoard


class Game:
    def __init__(self, player='white'):
        self.board = createBoard(player=player)

    def draw(self, screen):
        self.board.draw(screen)
        self.board.drawPieces(screen)


def createGame(player='white'):
    return Game(player=player)
