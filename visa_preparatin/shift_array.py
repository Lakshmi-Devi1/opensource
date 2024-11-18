def rotate_array(arr, K):
    N = len(arr)
    K = K % N
    rotated_array = arr[-K:] + arr[:-K]
    return rotated_array
N = int(input())  
arr = list(map(int, input().split()))
K = int(input())  
result = rotate_array(arr, K)
print(*result)
