class Solution:
    def first_n_fibonacci_recursion(self, counter) -> int:
        if counter == 1 or counter == 2:
            return 1
        return self.first_n_fibonacci_recursion(self, counter - 1) + self.first_n_fibonacci_recursion(self, counter - 2)

    def first_n_fibonacci_recursion_memoized(self, counter,cached:dict) -> int: #storing the values of already computed things

        if cached.get(counter):
            return cached.get(counter)
        if counter == 1 or counter == 2:
            return 1

        sum = self.first_n_fibonacci_recursion_memoized(self, counter - 1,cached) + self.first_n_fibonacci_recursion_memoized(self, counter - 2,cached)

        cached[counter] = sum
        return sum

    def first_n_fibonacci_recursion_memoized_with_array(self, counter, memo) -> int:  # storing the values of already computed things

        if memo[counter] :
            return memo[counter]
        if counter == 1 or counter == 2:
            return 1
        else:
            sum = self.first_n_fibonacci_recursion_memoized_with_array(self, counter - 1) + self.first_n_fibonacci_recursion_memoized_with_array(self, counter - 2)

        memo[counter] = sum
        return sum


def first_n_fibonacci_recursion_memoized_with_array( counter, memo) -> int:  # storing the values of already computed things

    if memo[counter] :
        return memo[counter]
    if counter == 1 or counter == 2:
        return 1
    else:
        sum = first_n_fibonacci_recursion_memoized_with_array( counter - 1) + first_n_fibonacci_recursion_memoized_with_array( counter - 2)

    memo[counter] = sum
    return sum


def bottom_up_approach_fibonacci(counter:int)-> int:

    array_to_store_computation = [0] * ( counter +1)

    array_to_store_computation[0],array_to_store_computation[1] = 1,1

    for i in range(2,counter+1):
        array_to_store_computation[i]=  array_to_store_computation[i-1] +  array_to_store_computation[i-2]

    return array_to_store_computation[counter-1]




if __name__ == '__main__':
    n = 100

    #print(Solution.first_n_fibonacci_recursion(Solution, n))

    #print(Solution.first_n_fibonacci_recursion_memoized(Solution, n,{}))

    #arr_cache = [None] * (n+1)

    #print(Solution.first_n_fibonacci_recursion_memoized_with_array(Solution, n, arr_cache))

    print(bottom_up_approach_fibonacci(n))

