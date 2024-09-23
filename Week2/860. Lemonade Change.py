def lemonadeChange(bills):
    change = [0] * 3
    for i in range(len(bills)):
        if i == 0 and bills[i] > 5:
            return False
        else:
            if bills[i] == 5:
                change[0] += 1
            elif bills[i] == 10:
                if change[0] > 0:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False
            else:
                if change[1] > 0 and change[0] > 0:
                    change[1] -= 1
                    change[0] -= 1
                elif change[0] > 2:
                    change[0] -= 3
                else:
                    return False
    return True


print(lemonadeChange([5, 5, 5, 10, 20]))  # --> true
print(lemonadeChange([5, 5, 10, 10, 20]))  # --> false
print(lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))  # --> false
print(lemonadeChange([10, 5, 5]))  # --> false

print(lemonadeChange([5, 10, 5, 20]))  # --> true
