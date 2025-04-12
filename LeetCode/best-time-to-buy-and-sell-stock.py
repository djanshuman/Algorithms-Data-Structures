class Solution:
    def maxProfit(self, prices) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit


if __name__ == "__main__":
    prices = [7,6,4,3,1]
    obj = Solution()
    print(obj.maxProfit(prices))
