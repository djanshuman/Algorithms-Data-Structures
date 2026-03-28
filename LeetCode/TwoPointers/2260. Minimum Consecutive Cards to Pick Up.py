'''
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
'''

'''
Approach 1 , using dictionary teleport method
'''

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        last_seen = dict()
        for r,card in enumerate(cards):
        
            if card in last_seen:
                min_window = r - last_seen[card] + 1
                min_len = min(min_len, min_window)

            last_seen[card] =  r


        return min_len if min_len != float('inf') else -1


'''
Approach 2 , using Set (less performant then App 1
'''

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        l = 0
        last_seen = set()
        for r in range(len(cards)):
            card = cards[r]

            while card in last_seen:
                min_len = min(min_len, r - l + 1)
                last_seen.remove(cards[l])
                l += 1

            last_seen.add(card)


        return min_len if min_len != float('inf') else -1
