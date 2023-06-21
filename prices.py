"""
 list_input, represents the price of the products.
 K, represents the given value K.
"""


def totalLuckyCustomer(list_input, K):
    prices = set(list_input)
    memoize = {}

    def savePreviousStates(price):

        if price in memoize:
            return memoize[price]

        count = 0

        if price - K in prices:
            count += 1

        memoize[price] = count

        return count

    total_count = 0

    for price in list_input:
        total_count += savePreviousStates(price)

    # Write your code here

    return total_count


def main():
    # input for list_input
    list_input = []
    list_input_size = int(input())
    list_input = list(map(int, input().split()))

    # input for K
    K = int(input())

    result = totalLuckyCustomer(list_input, K)
    print(result)

def find_gift_basket_lucky_customers( list_input, K):

  # Create a dictionary to store the number of times each price appears in the list.
  price_count_dict = {}
  for price in list_input:
    if price not in price_count_dict:
      price_count_dict[price] = 0
    price_count_dict[price] += 1

  # Find the number of lucky customers who will win a gift basket.
  lucky_customers = 0
  for price in price_count_dict:
    if price + K in price_count_dict:
      lucky_customers += price_count_dict[price] * price_count_dict[price + K]

  return lucky_customers



def find_gift_basket_lucky_customers1( list_input, K):


    price_count_dict = {}

    # Count the occurrences of each price
    for price in list_input:
        price_count_dict[price] = price_count_dict.get(price, 0) + 1

    lucky_customers = 0

    # Find the number of lucky customers
    for price in price_count_dict:
        if price + K in price_count_dict:
            lucky_customers += price_count_dict[price] * price_count_dict[price + K]

    return lucky_customers
if __name__ == "__main__":

    list_input = [3,6,15,9,6,15,3]
    K = 6

    # list_input = [10, 15, 23, 14, 2, 15]
    # K = 13
    #result = totalLuckyCustomer(list_input, K)
    result = find_gift_basket_lucky_customers1(list_input, K)
    print(result)

    #main()