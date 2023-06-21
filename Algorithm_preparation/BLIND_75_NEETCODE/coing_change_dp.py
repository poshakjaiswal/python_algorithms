from typing import  List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1] * (amount+1)
        dp[0] = 0


        for i in range(1,amount+1):
            for _i,v in enumerate(coins):#minimum number of coins
                if i - v >= 0:
                    dp[i] = min(dp[i],1 + dp[i-v])

        return dp[amount] if dp[amount]< amount else -1


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11

    print(Solution.coinChange(Solution,coins,amount))

