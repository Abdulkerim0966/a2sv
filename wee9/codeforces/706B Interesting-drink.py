from bisect import bisect_left, bisect_right


no_shops=int(input())
li = list (map(int, input().split()))
no_days = int (input())
li.sort()

for i in range(no_days):
    mo=int(input())
    idx=bisect_right(li,mo)

    print(idx)