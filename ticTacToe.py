import numpy as np
from enum import Enum
from random import choice
import minimax

winMat = [[(0, 0), (0, 1), (0, 2)],
          [(1, 0), (1, 1), (1, 2)],
          [(2, 0), (2, 1), (2, 2)],
          [(0, 0), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (2, 1)],
          [(0, 2), (1, 2), (2, 2)],
          [(0, 0), (1, 1), (2, 2)],
          [(0, 2), (1, 1), (2, 0)]]

class Glyph(Enum):
    x = 'X'
    o = 'O'
    empty = '-'

class Player:

    def __init__(self, glyph):
        self.glyph = glyph

    def makeMove(self):
        pass

    def checkMove(self, boardState, x, y):

        if boardState[x][y] == Glyph.empty:
            return True
        else:
            return False

    def getLegalMoves(self, boardState):

        legalMoves = []

        for i in range(0, len(boardState)):
            for j in range(0, len(boardState[i])):
                if boardState[i][j] == Glyph.empty:
                    legalMoves.append((i, j))
                    
        return legalMoves

class HumanPlayer(Player):

    def makeMove(self, boardState):
        
        x = int(input('Input X Coord (0 - 2)'))
        y = int(input('Input Y Coord (0 - 2)'))

        while not self.checkMove(boardState, x, y) or (x < 0 or x > 2) or (y < 0 or y > 2):

            print('Invalid Input, out of range or square is taken')

            x = int(input('Input X Coord (0 - 2)'))
            y = int(input('Input Y Coord (0 - 2)'))
            
        boardState[x][y] = self.glyph
        return boardState

class ComputerPlayer(Player):

    def __init__(self, glyph):
        self.mm = MiniMaxer()

    def makeMove(self, boardState):

        print('Computer Moving')

        legalMoves = self.getLegalMoves(boardState)

        try:
            x, y = choice(legalMoves)
            boardState[x][y] = self.glyph
            return boardState
        except:
            print('No Legal Moves')
            return boardState

        

class Board:

    def __init__(self, boardState = None):

        if boardState is None:
            self.boardState = np.ndarray(shape = (3, 3), dtype = Glyph)

            for i in range(0, len(self.boardState)):
                for j in range(0, len(self.boardState[i])):
                    self.boardState[i][j] = Glyph.empty

        else:
            self.boardState = boardState

    def __str__(self):

        s = ''

        for row in self.boardState:
            for cell in row:
                s += cell.value + '  '
            s += '\n'
        return s

class TicTacToeGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.turn = 1
        self.gameOver = False
        self.winner = Glyph.empty

        self.board = Board()

    def toggleTurn(self):
        self.turn *= -1

    def getCurrentPlayer(self):
        if self.turn > 0:
            return self.player1
        else:
            return self.player2

    def legalMovesExist(self):
        b = self.board.boardState
        for row in b:
            for cell in row:
                if cell == Glyph.empty:
                    return True
        return False

    def checkForWinners(self):

        b = self.board.boardState
        checks = [Glyph.x, Glyph.o]

        for check in checks:

            for winCond in winMat:

                x = winCond[0]
                y = winCond[1]
                z = winCond[2]
                
                if check == b[x[0]][x[1]] == b[y[0]][y[1]] == b[z[0]][z[1]]:
                    return check

        return Glyph.empty

    def playGame(self):

        while not self.gameOver:

            print(self.board)

            self.getCurrentPlayer().makeMove(self.board.boardState)

            self.winner = self.checkForWinners()
            print(self.winner)

            if (not self.winner == Glyph.empty) or (not self.legalMovesExist):
                self.gameOver = True

            self.toggleTurn()

        
        print(self.board)

        if self.winner == Glyph.empty:
            print('Tie!')
        else:
            print('{0} Wins!'.format(self.winner.value))
            
        

if __name__ == '__main__':

    # Test
    p1 = HumanPlayer(Glyph.x)
    p2 = ComputerPlayer(Glyph.o)

    game = TicTacToeGame(p1, p2)
    game.playGame()
