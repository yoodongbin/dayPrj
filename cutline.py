N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
print(arr.pop(M-1))