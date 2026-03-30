'''
https://leetcode.com/problems/range-sum-query-immutable/description/

A cleaner real-world design would be a class that builds prefix sum once:
pythonclass RangeSumQuery:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def query(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    left = int(input())
    right = int(input())
    rsq = RangeSumQuery(nums)
    print(rsq.query(left, right))


'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]

    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1 ] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


