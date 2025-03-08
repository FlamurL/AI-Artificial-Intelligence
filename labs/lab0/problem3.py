import random
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)

class Player:
    def __init__(self):
        self.x=0
        self.y=0


    def move(self, pos):
        self.x=pos[0]
        self.y=pos[1]
        print(f"[{self.x, self.y}]")


class Game:
    def __init__(self, table, n, m):
        self.table = [list(row) for row in table]  # Convert each row to a list of characters
        self.width = n
        self.height = m
        self.dotsCount = sum(row.count('.') for row in table)
    
    def print_table(self):
        for row in self.table:
            print(''.join(row))  # Convert back to string when printing


class Pacman:
    def __init__(self, player,game):
        self.player=player
        self.game=game



    def get_movesThatAreValid(self):
        validMoves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dx, dy in directions:
            nRow = self.player.x + dx
            nColumn = self.player.y + dy
            if 0 <= nRow < self.game.height and 0 <= nColumn < self.game.width:
                validMoves.append((nRow, nColumn))
        return validMoves
        

    def get_movesThatAreValidDots(self, validMoves):
        return[(row, column) for row,column in validMoves if self.game.table[row][column]=='.']
    
    

    def eatenDot(self, nextMove):
        self.game.table[nextMove[0]][nextMove[1]] = '#'


    def play_game(self):
        if self.game.dotsCount == 0:
            print("Nothing to do here")
            return

        while self.game.dotsCount > 0:
            movesThatAreValid = self.get_movesThatAreValid()
            movesThatAreValidDots = self.get_movesThatAreValidDots(movesThatAreValid)

            if movesThatAreValidDots:
                nextMove = random.choice(movesThatAreValidDots)
                self.eatenDot(nextMove)
                self.player.move(nextMove)
                self.game.dotsCount -= 1
            else:
                nextMove = random.choice(movesThatAreValid)
                self.player.move(nextMove)



if __name__ == "__main__":
    width=int(input())
    height=int(input())
    table=[]
    for i in range(width):
        row=list(input())
        table.append(row)


    player=Player()
    game=Game(table,width,height)

    pacman = Pacman(player,game)
    pacman.play_game()
        