
maxn = 179 * 1000
ans = 0
for i in range(maxn + 1):
    if i % 2 == 1:
        ans += i * i
print(ans)