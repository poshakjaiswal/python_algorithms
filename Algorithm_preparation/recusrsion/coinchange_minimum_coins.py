from typing import List
class Coins:
    def findMinimumCoinsForSum(self, targetSum,inputCoins) -> List:
        # base case
        if 0 == targetSum:
            return collected.add(sofar)

        # break string into two parts and swap them
        for i in range(0, len(remaining)):
             #pick one character
            picked_character = remaining[i]
            rest = remaining[0: i] + remaining[i + 1:]
            self.permute(self,rest,sofar + picked_character,collected)

        print(collected)
        return len(collected)



if __name__ == '__main__':
    targetSum = 30
    inputCoins =[ ]
    print(Coins.findMinimumCoinsForSum(Coins,targetSum,inputCoins))
