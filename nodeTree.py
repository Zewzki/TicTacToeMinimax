import numpy as np
from ticTacToe import Glyph
from ticTacToe import winMat
from ticTacToe import ComputerPlayer
from ticTacToe import TicTacToeGame

def getLegalMoves(boardState):

        legalMoves = []

        for i in range(0, len(boardState)):
            for j in range(0, len(boardState[i])):
                if boardState[i][j] == Glyph.empty:
                    legalMoves.append((i, j))
                    
        return legalMoves

def getWinner(b):

    checks = [Glyph.x, Glyph.o]

    for check in checks:

        for winCond in winMat:

            x = winCond[0]
            y = winCond[1]
            z = winCond[2]
                
            if check == b[x[0]][x[1]] == b[y[0]][y[1]] == b[z[0]][z[1]]:
                return check

    return Glyph.empty

class Node:

    maxDepth = 9

    def __init__(self, boardState = None, playerToMove, depth):
            
        self.value = 0
        self.playerToMove = playerToMove
        self.winner = getWinner(boardState)
        self.legalMoves = getLegalMoves(boardState)
        self.childNodes = None
        self.boardState = boardState
        self.depth = depth

        if playerToMove > 0:
            self.glyph = Glyph.x
        else:
            self.glyph = Glyph.o

    def recursivelyFillTree(self):

        if self.depth >= self.maxDepth:
            return

        self.populateChildren()

        for childNode in self.childNodes:
            childNode.recursivelyFillTree()

    def populateChildren(self):

        self.childNodes = []

        for move in self.legalMoves:
            newBoard = np.copy(self.boardState)
            newBoard[move[0]][move[1]] = self.glyph
            self.childNodes.append(Node(newBoard, self.playerToMove * -1, self.depth + 1))



if __name__ == '__main__':

    p1 = ComputerPlayer(Glyph.x)
    p2 = ComputerPlayer(Glyph.o)
    game = TicTacToeGame(p1, p2)

    root = Node(game.board.boardState, 1, 0)
    root.recursivelyFillTree()
