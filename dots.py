import os
import time
import colorama
from colorama import Fore

class GameState:
    def __init__(self, gridsize, players):
        self.gridsize = gridsize
        self.maxmoves = gridsize*(gridsize-1)*2
        self.grid = [[0]*(gridsize*2-1) for i in range(gridsize*2-1)]
        self.movesmade=0
        self.scores = [0]*players
        self.players = players

def main():
    gs = input("gridsize (min 2): ")

    g = GameState(int(gs),2)
    curplayer = 0
    while True:
        
        if curplayer == 1:
            time.sleep(2)

            os.system('cls' if os.name == 'nt' else 'clear')
            move = aiMove(g)
            print("ai wants to make move " + str(move))
            m = str(move[0]) + "," + str(move[1])
            doMove(m,g,curplayer+1)
            curplayer = nextPlayer(curplayer, g)
            print_board(g.gridsize, g.grid)
            continue

        doMove(input("player " + str(curplayer+1) + " move: "),g, curplayer+1)
        print_board(g.gridsize, g.grid)
        curplayer = nextPlayer(curplayer, g)

def nextPlayer(cur, g):
    return (cur+1)%g.players

def checkEnclosed(x,y,g):
    #print(getBordered(x,y,g))
    ps = getBordered(x,y,g)
    if ps[0] >= 0 and ps[0] < g.gridsize*2-1 and ps[1] >= 0 and ps[1] < g.gridsize*2-1:
        if (isEnclosed(ps[0],ps[1],g)):
            return True
    
    if ps[2] >= 0 and ps[2] < g.gridsize*2-1 and ps[3] >= 0 and ps[3] < g.gridsize*2-1:
        if isEnclosed(ps[2],ps[3],g):
            return True 
    return False 

def isEnclosed(x,y,g):
    return g.grid[y+1][x] > 0 and g.grid[y-1][x] > 0 and g.grid[y][x-1] > 0 and g.grid[y][x+1] > 0
        
def getBordered(x,y,g):
    if direction(y) == 1:
        return (y,x-1,y,x+1)
    else:
        return (y-1,x,y+1,x)

def countBorders(x,y,g):
    count=0
    if g.grid[y+1][x] > 0:
        count+=1
    if g.grid[y-1][x] > 0:
        count+=1
    if g.grid[y][x-1] > 0:
        count+=1
    if g.grid[y][x+1] > 0:
        count+=1
    return count

def aiMove(g):
    print("Ai waiting for dramatic effect")
    time.sleep(1)
    moves = {}
    for x in range(1,g.gridsize*2-1,2):
        for y in range(1,g.gridsize*2-1,2):
            score = 4-countBorders(y,x,g)
            if score == 2:
                score = 1000
            if score == 0:
                continue
            moves[(y,x)] = score
    move = min(moves, key=moves.get)
    print("move scored: " + str(moves[move]))
    print("placing around square " + str(move))
    if g.grid[move[1]-1][move[0]] == 0:
        return [move[0],move[1]-1]
    elif g.grid[move[1]+1][move[0]] == 0:
        return [move[0],move[1]+1]
    elif g.grid[move[1]][move[0]-1] == 0:
        return [move[0]-1,move[1]]
    elif g.grid[move[1]][move[0]+1] == 0:
        return [move[0]+1,move[1]]
    print("no good")
    exit()
    return move

def direction(y):
    return y%2

def end_game(g):
    winner = g.scores.index(max(g.scores))
    print("player " + str(winner + 1) + " wins !!! : )")
    print_board(g.gridsize,g.grid)
    resp = input("play again : ) ?????????? (y/n): ")
    if resp[0] == 'y':
        main()
    exit()

def doMove(m, g, player):
    if g.movesmade == g.maxmoves:
        end_game(g)
    m = m.split(",")
    x = int(m[0])
    y = int(m[1])
    
    if (x + y)%2 != 1:
        print("not edge")
        doMove(input("move: "),g, player)
        return
    if g.grid[y][x] != 0:
        print("illegal move")
        doMove(input("move: "),g, player)
        return
    
    g.movesmade+=1
    g.grid[y][x] = int(player)
    if checkEnclosed(y,x,g):
        g.scores[player-1] +=1
        if g.movesmade == g.maxmoves:
            end_game(g)

        print("player " + str(player) + " gets point, another turn")

        print_board(g.gridsize, g.grid)
        if (player == 2):
            move = aiMove(g)
            print("ai wants to make move " + str(move))
            m = str(move[0]) + "," + str(move[1])
            doMove(m,g,player)
            return
        doMove(input("move: "),g, player)
        

def print_board(gridsize,a):
    i = 1
    printH = 1 
    h_or_v = 0#takes the rigth array
    for line in range(0,gridsize*2-1):
        if (printH == 1):
            for part in range(0,gridsize-1):
                h=a[h_or_v]#horizontal lines
                print(Fore.WHITE+'*', end = " ")
                if h[i] == 1:
                    print(Fore.RED+'-----', end = " ")
                elif h[i] == 2:
                    print(Fore.BLUE +'-----', end = " ")
                else:
                    print('     ', end = " ")
                i=i+2
            print(Fore.WHITE+'*')
            i = 0 #for vertical
            printH = 0
            h_or_v += 1
            one_m= ''
        elif(printH == 0):
            for part in range(0,gridsize-1):
                v=a[h_or_v]
                if v[i] == 1:
                    print(Fore.RED+'|', end = " ")
                    one_m += Fore.RED+"|       "
                elif v[i] == 2:
                    print(Fore.BLUE+'|', end = " ")
                    one_m += Fore.BLUE+"|       "
                else:
                    print(' ', end = " ") 
                    one_m += "        "
                print("     ", end = " ")
                i=i+2
                
            if v[i] == 1:
                print(Fore.RED+'|')
                one_m += Fore.RED+'|'
            elif v[i] == 2:
                print(Fore.BLUE+'|')
                one_m += Fore.BLUE+'|'
            else:
                print(' ') 
            print(one_m)
            
            i= 1
            h_or_v += 1
            printH = 1     
    print(Fore.RESET + " \n")

if __name__ == "__main__":
    main()
