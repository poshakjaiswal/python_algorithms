from typing import List

class Solution:


    def find_unique_paths_in_grid_recursively(self, m:int, n:int )-> int:

        if m == 0 or n== 0:
            return 0
        elif m ==1 or n == 1:
            return 1

        return self.find_unique_paths_in_grid_recursively(self,m-1,n ) + self.find_unique_paths_in_grid_recursively(self,m,n-1 )






if __name__ == '__main__':

    m = 3
    n = 4

    print( Solution.find_unique_paths_in_grid_recursively(Solution,m,n))

