# O(N) - сложность алгоритма

a = [int(x) for x in input().split()][::-1]
S = int(input())
count = 0
for coin in a:
    newcount = S // coin
    print(f'coin {coin} = {newcount}')
    count += newcount
    S %= coin
print(count)
