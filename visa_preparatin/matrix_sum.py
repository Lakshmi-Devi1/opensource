def matrix_sum(matrix, N):
    A = []
    for i in range(N):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(N))
        A.append(row_sum + col_sum)
    return A
N = int(input()) 
matrix = []
for _ in range(N):
    row = list(map(int, input().split())) 
    matrix.append(row)
result = matrix_sum(matrix, N)
print(*result)
