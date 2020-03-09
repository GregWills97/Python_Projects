import numpy as np #use numpy for better matrix printing

class Grid:

    def __init__(self):
        #self.grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        #             [6, 0, 0, 1, 9, 5, 0, 0, 0],
        #             [0, 9, 8, 0, 0, 0, 0, 6, 0],
        #             [8, 0, 0, 0, 6, 0, 0, 0, 3],
        #             [4, 0, 0, 8, 0, 3, 0, 0, 1],
        #             [7, 0, 0, 0, 2, 0, 0, 0, 6],
        #             [0, 6, 0, 0, 0, 0, 2, 8, 0],
        #             [0, 0, 0, 4, 1, 9, 0, 0, 5],
        #             [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        
        self.grid = [[1, 0, 0, 4, 8, 9, 0, 0, 6],
                     [7, 3, 0, 0, 0, 0, 0, 4, 0],
                     [0, 0, 0, 0, 0, 1, 2, 9, 5],
                     [0, 0, 7, 1, 2, 0, 6, 0, 0],
                     [5, 0, 0, 7, 0, 3, 0, 0, 8],
                     [0, 0, 6, 0, 9, 5, 7, 0, 0],
                     [9, 1, 4, 6, 0, 0, 0, 0, 0],
                     [0, 2, 0, 0, 0, 0, 0, 3, 7],
                     [8, 0, 0, 5, 1, 2, 0, 0, 4]]
        
        #self.grid = [[4, 3, 5, 2, 6, 0, 7, 0, 1],
        #             [6, 8, 2, 0, 7, 0, 0, 9, 0],
        #             [1, 9, 0, 0, 0, 4, 5, 0, 0],
        #             [8, 2, 0, 1, 0, 0, 0, 4, 0],
        #             [0, 0, 4, 6, 0, 2, 9, 0, 0],
        #             [0, 5, 0, 0, 0, 3, 0, 2, 8],
        #             [0, 0, 9, 3, 0, 0, 0, 7, 4],
        #             [0, 4, 0, 0, 5, 0, 0, 3, 6],
        #             [7, 0, 3, 0, 1, 8, 0, 0, 0]]
    
    def Valid(self, y, x, n) :
        for i in range(0,9) :         
            if self.grid[y][i] == n :    #Look at the entire row to check valid input
                return False
        for i in range(0,9) :
            if self.grid[i][x] == n :    #Look at the entire column to check valid input
                return False
    
        u = (x//3)*3    #u and v used to check the square n will be placed in
        v = (y//3)*3
        
        for i in range(3) :
            for j in range(3) :     #nested for-loop to check square
                if self.grid[v + i][u + j] == n :
                    return False
        return True     #if valid placement return true
    
    def Solve(self) :   #function that solves puzzle using backtracking
        for y in range(9) :
            for x in range(9) :
                if self.grid[y][x] == 0 :
                    for n in range(1,10) :
                        if self.Valid(y, x, n) :
                            self.grid[y][x] = n
                            self.Solve()
                            self.grid[y][x] = 0  #if solve returns set to zero and "backtrack" to find different solution
                            #updateScreen()
                    return
        print(np.matrix(self.grid))
        #hold for confirm
        return self
