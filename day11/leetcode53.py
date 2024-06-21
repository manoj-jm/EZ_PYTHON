matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
res = []

while top <= bottom and left <= right:
    # Traverse from left to right
    for i in range(left, right + 1):
        res.append(matrix[top][i])
    top += 1

    # Traverse from top to bottom
    for i in range(top, bottom + 1):
        res.append(matrix[i][right])
    right -= 1

    # Traverse from right to left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1

    # Traverse from bottom to top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1


print(res)