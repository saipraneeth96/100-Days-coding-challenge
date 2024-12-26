Day 74 coding Statement:

You have a grid with N rows and M columns. You have two types of tiles — one of dimensions 2×2 and the other of dimensions 1×1. You want to cover the grid using these two types of tiles in such a way that:

Each cell of the grid is covered by exactly one tile; and
The number of 1×1 tiles used is minimized.
Find the minimum number of 1×1 tiles you have to use to fill the grid.



t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    
    # Count how many full 2x2 tiles can fit
    two_by_two_tiles = (N // 2) * (M // 2)
    
    # Calculate remaining uncovered rows and columns
    remaining_rows = N % 2
    remaining_cols = M % 2
    
    # Calculate the remaining uncovered cells
    remaining_cells = (remaining_rows * M) + (remaining_cols * (N - remaining_rows))
    
    # Print the number of 1x1 tiles required
    print(remaining_cells)
