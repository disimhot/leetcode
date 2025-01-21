from collections import deque
class Solution(object):
    def __init__(self):
        self.n = None
        self.have_eaten = 0
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        self.n = len(students)
        ones = deque([x for x in students if x == 1])
        zeros = deque([x for x in students if x == 0])
        for i in range(len(sandwiches)):
            if sandwiches[i] == 1:
                if len(ones) == 0:
                    return self.n - self.have_eaten
                ones.popleft()
                self.have_eaten += 1
            else:
                if len(zeros) == 0:
                    return self.n - self.have_eaten
                zeros.popleft()
                self.have_eaten += 1

        return self.n - self.have_eaten

s1 = Solution()
s2 = Solution()
print(s1.countStudents([1,1,0,0], [0,1,0,1]))
print(s2.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))