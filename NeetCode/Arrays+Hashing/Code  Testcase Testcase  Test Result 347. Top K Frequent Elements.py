'''
 https://leetcode.com/problems/top-k-frequent-elements/
 
'''


'''Approach 1 
Time Complexity: O(n log n)

O(n) to build the frequency dictionary
O(n log n) to push all n elements onto the heap
O(k log n) to pop k times

Space Complexity: O(n)

O(n) for the dictionary
O(n) for the heap
'''


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        mydict = dict()

        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        
        for key,val in mydict.items():
            heapq.heappush(maxheap,(-val,key))

        res =[]
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        return res

'''Approach 2 
Optimised and preferred using bucket sort by frequency

Time Complexity: O(N)

O(N) to build the frequency dictionary
O(N) to build the buckets
O(N) to iterate through buckets

Space Complexity: O(N)

O(N) for the dictionary
O(N) for the buckets
O(N) for the result


'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = dict()

        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        
        # Use frequency bucket approach
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in mydict.items():
            buckets[val].append(key)
        #[[], [3], [2], [1], [], [], []]

        res = []
        for i in range(len(buckets) -1, -1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
    
