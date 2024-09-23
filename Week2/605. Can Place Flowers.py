def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True

    prev = -2
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) and (i != prev + 1):
            n -= 1
            prev = i
        if n == 0:
            return True
    return False


print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(canPlaceFlowers([0], 1))
