class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        else:
            memo = [0] * (n + 1)
            memo[1] = 1

            def count(n):
                main = n // 2
                remainder = n % 2
                if n == 0 or n == 1:
                    return memo[n]
                if memo[main]:
                    f1 = memo[main]
                else:
                    f1 = count(main)
                    memo[main] = f1
                if memo[remainder]:
                    f2 = memo[remainder]
                else:
                    f2 = count(remainder)
                    memo[remainder] = f2
                memo[n] = f1 + f2
                return f1 + f2

            for i in range(2, n + 1):
                res = count(i)
                memo[n] = res
            return memo


# print(countBits(2))
# print(countBits(3))
print(countBits(5))
