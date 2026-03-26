'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
''' O(n) preferred approach'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (l <= r):
            sum = numbers[l] + numbers[r]
            if sum == target and l != r:
                return [l+1,r+1]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
        return []


'''
Binary  Search O(nlogn)
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            compliment = target - numbers[i]

            l = i+1
            r = len(numbers) - 1
            while (l <= r):
                mid = (l + r) // 2
                if numbers[mid] == compliment:
                    return [i+1,mid+1]
                elif numbers[mid] < compliment:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
