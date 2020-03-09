from grid import Grid
import numpy as np #use numpy for better matrix printing

def Main():
    new = Grid()
    solve = Grid()
    solve = new.Solve()
    print(np.matrix(new.grid))

if __name__ == '__main__':
    Main()
