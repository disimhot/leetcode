def jump(nums):
    n = len(nums)
    count = 0
    real_max = 0  # локальный макс
    ireal_max = -1
    max = -1  # локальный макс, который будем уменьшать, чтобы находить другие

    # isupport - индекс опорного элемента
    # как только он равен нулю, вычитаем все ложные локальные максимумы, которые не нужны
    isupport = 0
    fake_count = 0

    if n == 0:
        return 0
    else:
        for i in range(n):
            if i == n - 1:
                return count
            if nums[i] > max:
                real_max, max, ireal_max = nums[i], nums[i], i
                count += 1
                if max + i >= n - 1:  # дошли до конца с любого элемента
                    return count - fake_count
                if isupport <= 0:  # опорный элемент, по которому считаем все ложные максимумы
                    isupport = real_max - i + ireal_max
                    count = count - fake_count
                    fake_count = 0
                    if fake_count > 0:
                        fake_count -= 1
                else:
                    fake_count += 1

            if isupport == 0:
                isupport = real_max - i + ireal_max
                if fake_count > 0:
                    fake_count -= 1
            max -= 1  # уменьшаем локальный макс чтобы находить другие
            isupport -= 1

        return count - fake_count

# print(jump([2, 9, 6, 5, 7, 0, 7, 2, 7, 9, 3, 2, 2, 5, 7, 8, 1, 6, 6, 6, 3, 5, 2, 2, 6, 3]))  # 5
# print(jump([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]))  # 4
# print(jump([4, 8, 4, 4, 9, 6, 9, 5, 5, 7, 1, 6, 7, 2, 1, 8]))  # 3
# print(jump([5, 4, 0, 1, 3, 6, 8, 0, 9, 4, 9, 1, 8, 7, 4, 8]))  # 3
# print(jump([9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]))  # 3
# print(jump([2, 0, 8, 0, 3, 4, 7, 5, 6, 1, 0, 0, 5, 9, 7, 5, 3, 6]))  # 4
# print(jump([1, 1, 1, 1, 1]))  # 4
# print(jump([9, 7, 9, 4, 8, 1, 6, 1, 5, 6, 2, 1, 7, 9, 0]))  # 2
# print(jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))  # 2
# print(jump([1, 2, 0, 1]))  # 2
# print(jump([2, 3, 1]))  # 1
# print(jump([4, 1, 1, 3, 1, 1, 1]))  # 2
# print(jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))  # 2
# print(jump([3, 4, 3, 2, 5, 4, 3]))  # 3
# print(jump([2, 3, 1, 1, 4]))  # 2


# Мое первое решение. Не прошел по времени для большого теста
#
# def jump(nums):
#     n = len(nums)
#     count = 0
#
#     if n == 0 or n == 1:
#         return 0
#
#     elif n == 2:
#         return 1
#     else:
#         i = 0
#         j = nums[0] + 1
#         a = nums[i:j]
#         temp = 0
#         temp_index = 0
#         diff = 1001
#
#         while i < n - 1:
#             for k in range(len(a)):
#                 if k + i == n - 1:
#                     return count + 1
#                 if (n - a[k] - k) < diff:
#                     diff = n - a[k] - k
#                     temp = a[k]
#                     temp_index = k
#
#             if temp_index != 0:
#                 i += temp_index
#             else:
#                 i += temp
#             j = min(temp + i + 1, n)
#             a = nums[i:j]
#
#             count += 1
#             diff = 1001
#         return count
