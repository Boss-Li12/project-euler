# 状态转移
# (a2, a3, a4, a5)
# (1, 1, 1, 1) -> (0, 0, 0, 1)
# 每次分裂增加比自己小的所有页面（因为要拿掉一个a5) <- 概率转移
# 期望就是概率的链式叠加
# 一张纸的状态需要加一下
from functools import lru_cache

@lru_cache
def dfs(state):
    if state == (0, 0, 0, 1): # 最后一批不算
        return 0
    lst = list(state)
    s = sum(lst)
    res = 0.0
    if s == 1:
        res = 1.0
    # 考虑概率转移
    for i in range(4):
        lst_copy = lst[:]
        pi = lst_copy[i] / s
        if lst_copy[i] > 0:
            lst_copy[i] -= 1
            for j in range(i + 1, 4):
                lst_copy[j] += 1
            res += pi * dfs(tuple(lst_copy))
    return res

print(f'{dfs((1, 1, 1, 1,)):.6f}')
            


