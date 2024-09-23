# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden digits.
def maximumTime(time):
    h, m = time.split(':')
    h = list(h)
    m = list(m)
    if h[0] == '?' and h[1] == '?':
        h[0] = '2'
        h[1] = '3'
    if h[0] == '?':
        if h[1] != '?' and int(h[1]) < 4:
            h[0] = '2'
        else:
            h[0] = '1'
    if h[1] == '?':
        if h[0] == '2':
            h[1] = '3'
        else:
            h[1] = '9'

    if m[0] == '?':
        m[0] = '5'
    if m[1] == '?':
        m[1] = '9'

    h = ''.join(h)
    m = ''.join(m)
    return f'{h}:{m}'


# print(maximumTime("00:??"))
# "00:59"

# print(maximumTime("0?:3?"))
# Output: "09:39"

# print(maximumTime("1?:22"))
# Output: "19:22"

print(maximumTime("?4:03"))
# "14:03"

print(maximumTime("?0:15"))
# "20:15"
