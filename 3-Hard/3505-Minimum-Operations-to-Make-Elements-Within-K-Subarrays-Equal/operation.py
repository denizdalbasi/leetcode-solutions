class Solution:
    def minOperations(self, nums, x, k):
        size = len(nums)
        cost = [0] * (size - x + 1)
        
        for i in range(len(cost)):
            subList = nums[i:i+x]
            subList.sort()
            total = 0
            median = subList[x // 2]
            for j in range(x):
                total += abs(median - subList[j])
            cost[i] = total 

        n_costs = len(cost)
        memo = {}

        def dp(i, count):
            if count == 0:
                return 0
            if i >= n_costs or (n_costs - i) < count * x:
                return float('inf')
            
            if (i, count) in memo:
                return memo[(i, count)]
            
            skip = dp(i + 1, count)
            take = cost[i] + dp(i + x, count - 1)
            
            memo[(i, count)] = min(skip, take)
            return memo[(i, count)]

        return dp(0, k)