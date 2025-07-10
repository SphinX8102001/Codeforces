import sys

boardSize = sys.stdin.readline().strip().split()
boardSize = [int(x) for x in boardSize]
m,n = boardSize[0],boardSize[1]
area = m*n
dominosArea = 2
required_num_of_domino = int(area/dominosArea)
print(required_num_of_domino)


