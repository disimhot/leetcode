class RecentCounter(object):
    def __init__(self):
        self.capacity = 3000
        self.requests = 0
        self.front = 0
        self.rear = -1
        self.queue = [None] * 10000
    def _enqueue(self, t):
        self.requests += 1
        self.rear = (self.rear + 1)
        self.queue[self.rear] = t

        while self.queue[self.front] < t - self.capacity:
            self.front = (self.front + 1)
            self.requests -= 1
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self._enqueue(t)
        return self.requests


# recentCounter.ping(1)
# recentCounter.ping(100)
# recentCounter.ping(3001)
# recentCounter.ping(3002)
# 1
# 2
# 3
# 3
