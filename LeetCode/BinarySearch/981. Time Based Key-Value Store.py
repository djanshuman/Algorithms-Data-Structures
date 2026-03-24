'''
https://leetcode.com/problems/time-based-key-value-store/description/
'''

class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap.keys():
            self.timemap[key] = []
        self.timemap[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap.keys():
            return ""
        pos = -1
        left = 0
        right = len(self.timemap[key]) -  1

        while (left <= right):
            mid = (left + right) // 2
            if self.timemap[key][mid][0] <= timestamp:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1

        if pos != -1:
            return self.timemap[key][pos][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
