n = int(input())
a = list(map(int, input().split()))
x = int(input())

close_el = a[0]

for num in a:
    if abs(num - x) < abs(close_el - x):
        close_el = num

print(close_el)