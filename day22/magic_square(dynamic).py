def is_magic_square(matrix):
    n = len(matrix)
    # Check if the matrix is a square matrix
    for row in matrix:
        if len(row) != n:
            return False

    # Calculate the sum of the first row to use as a reference
    reference_sum = sum(matrix[0])

    # Check sums of all rows
    for row in matrix:
        if sum(row) != reference_sum:
            return False

    # Check sums of all columns
    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        if col_sum != reference_sum:
            return False

    # Check main diagonal sum
    main_diagonal_sum = 0
    for i in range(n):
        main_diagonal_sum += matrix[i][i]
    if main_diagonal_sum != reference_sum:
        return False

    # Check secondary diagonal sum
    secondary_diagonal_sum = 0
    for i in range(n):
        secondary_diagonal_sum += matrix[i][n - 1 - i]
    if secondary_diagonal_sum != reference_sum:
        return False

    return True

def get_matrix():
    n = int(input("Enter the size of the matrix (n x n): "))
    matrix = []

    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
        if len(row) != n:
            print("Row length must be equal to the size of the matrix. Please try again.")
            return None
        matrix.append(row)
    
    return matrix

# Get the matrix from the user
matrix = get_matrix()

if matrix is not None:
    if is_magic_square(matrix):
        print("It is a Magic square")
    else:
        print("It is not a Magic square")
else:
    print("Invalid matrix input.")
