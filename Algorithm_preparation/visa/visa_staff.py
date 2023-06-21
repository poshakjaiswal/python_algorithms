import math


def solution(a):
    outPut = []
    outPut.append(-math.inf)

    left = 0
    right = len(a) -1
    index = 0



    while left <= right:

        last = outPut.pop()

        if (index%2 == 0):

            if last > a[left]:
                return False
            outPut.append(a[left])
            left = left+1

        else:
            if last > a[right]:
                return False
            outPut.append(a[right])
            right = right-1



        index = index + 1



    return True







if __name__ == '__main__':

    arr = [ 1,2,3,4,5,6,7,8]
    arr = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
    print(solution (arr))
