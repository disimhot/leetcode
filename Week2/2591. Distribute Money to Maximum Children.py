def distMoney(money, children):
    if money < children:
        return -1

    n = money // 8
    r = money % 8

    if n == children and r == 0:
        return n

    count = 0
    for i in range(children):
        money -= 8
        if i == (children - 1):  # если дошли до последн ребенка
            return count
        else:
            if money <= 0:
                return count
            elif money == 4 and (children - i - 1) == 1:  # если останется 4 дол последн ребенку
                return count
            elif money < (children - i - 1):
                return count
        count += 1
    return count


print(distMoney(16, 2))
# 2
print(distMoney(20, 3))
# 1
print(distMoney(2, 2))
# Output: 0
print(distMoney(8, 2))
# Output: 0
print(distMoney(8, 1))
# Output: 1
print(distMoney(12, 2))
# Output: 0
print(distMoney(12, 3))
# Output: 1
print(distMoney(9, 2))
# Output: 1
print(distMoney(16, 3))
# 1
print(distMoney(17, 3))
# # 2
print(distMoney(9, 3))
# 0
print(distMoney(16, 10))
# 0
print(distMoney(17, 2))
# 1
print(distMoney(24, 11))
# 1
