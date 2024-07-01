# def is_safe(board, row, col, n):
#     # Check this row on left side
#     for i in range(col):
#         if board[row][i] == 1:
#             return False

#     # Check upper diagonal on left side
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     # Check lower diagonal on left side
#     for i, j in zip(range(row, n, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     return True

# def solve_n_queens_util(board, col, n):
#     # If all queens are placed, return true
#     if col >= n:
#         return True

#     # Consider this column and try placing this queen in all rows one by one
#     for i in range(n):
#         if is_safe(board, i, col, n):
#             board[i][col] = 1

#             if solve_n_queens_util(board, col + 1, n):
#                 return True

#             board[i][col] = 0

#     return False

# def solve_n_queens(n):
#     board = [[0 for _ in range(n)] for _ in range(n)]

#     if not solve_n_queens_util(board, 0, n):
#         print("Solution does not exist")
#         return False

#     print_solution(board)
#     return True

# def print_solution(board):
#     for row in board:
#         print(" ".join("Q" if cell else '0' for cell in row))

# # Example usage
# n = 4
# solve_n_queens(n) 


def fun(board , row):
  if row == n:
    print(board)
  for col in range(0,n):
    if safePosition(board,row,col)==True: 
      board[row][col]=1
      fun(board,row+1)
    board[row][col] = 0



















