# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

def balancedStringSplit(s):
    count = 0
    isBalanced = 0
    for i in range(len(s)):
        if s[i] == 'R':
            isBalanced += 1
        else:
            isBalanced -= 1
        if isBalanced == 0:
            count += 1
    return count


print(balancedStringSplit('RLRRLLRLRL'))  # 4
print(balancedStringSplit('RLRRRLLRLL'))  # 2
print(balancedStringSplit('LLLLRRRR'))  # 1
