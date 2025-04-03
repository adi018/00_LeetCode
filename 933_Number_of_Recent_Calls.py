class RecentCounter:

    def __init__(self):
        self._q = []
        

    def ping(self, t: int) -> int:
        start = t - 3000
        end = t
        self._q.append(t)
        while self._q[0] < start:
            self._q.pop(0)
        return len(self._q)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)