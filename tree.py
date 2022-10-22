n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
maxdays = 0
for i in range(n):
    maxdays = max(maxdays, arr[i] + i + 1)
print(maxdays + 1)