import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._counter = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._counter, item))
        self._counter += 1

    def pop(self):
        return heapq.heappop(self._queue)[1]

