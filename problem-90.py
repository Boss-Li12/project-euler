from itertools import combinations

def solve():
    targets = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]
    numbers = list(range(10))
    combs = list(combinations(numbers, 6))
    
    def check(s1, s2):
        if 6 in s1:  
            s1.add(9)
        if 9 in s1:
            s1.add(6)
        if 6 in s2:
            s2.add(9)
        if 9 in s2:
            s2.add(6)
        for a, b in targets:
            if not ((a in s1 and b in s2) or (a in s2 and b in s1)):
                return False
        return True
    
    cnt = 0
    n = len(combs)
    for i in range(n):
        for j in range(i + 1, n):
            if check(set(combs[i]), set(combs[j])):
                cnt += 1
    print(cnt)

solve()