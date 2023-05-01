import copy
import time
import matplotlib.pyplot as plt
import numpy as np


def solveNQueens(n):
    board = [["." for i in range(n)] for i in range(n)]
    cols = set()
    diags = set()
    antiDiags = set()
    ret = []

    def checkCols(col):
        if col in cols:
            return False
        return True

    def checkDiagonals(row, col):
        if (row - col) in antiDiags or (row + col) in diags:
            return False
        return True

    def drawBoard():
        tmp = []
        for row in board:
            tmp.append("".join(row))
        ret.append(copy.deepcopy(tmp))

    def dfs(row):
        global caller
        caller += 1
        if row == n:
            drawBoard()
            return
        for i in range(n):
            if checkCols(i) and checkDiagonals(row, i):
                cols.add(i)
                antiDiags.add(row - i)
                diags.add(row+i)
                board[row][i] = "Q"
                dfs(row+1)
                board[row][i] = '.'
                cols.remove(i)
                antiDiags.remove(row - i)
                diags.remove(row+i)
    dfs(0)
    return caller


times = {}
calls = {}
numbers = {}
for i in range(20):
    caller = 0
    start = time.time()
    caller = solveNQueens(i)
    calls[i] = caller
    end = time.time()
    times[i] = end-start
    numbers[i] = i
    print(i, "---", end-start, "---", caller)

y = np.array(times.values())
x = times.keys()

plt.plot(x, y)


plt.xlabel("value of N")
plt.ylabel("Time taken")
plt.title('time to N queens')
plt.show()

y = np.array(calls.values())
x = calls.keys()

plt.plot(x, y)


plt.xlabel("value of N")
plt.ylabel("nodes of the recursion tree")
plt.title('nodes to N queens')
plt.show()