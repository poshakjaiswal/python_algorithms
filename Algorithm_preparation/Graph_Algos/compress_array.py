

def getMinLength(a, k):
    tempProducts = []

    # put a base case check if lenght is only 2
    leftPointer = 0
    rightPointer = 1

    currentProduct = 1
    a.append(1)

    def productUptoN(arr, start, end):

        product = 1

        for i in range(start, end):
            product = product * arr[i]

        return product

    for elem in a:

        # print(currentProduct)

        currentProduct = currentProduct * elem

        if (currentProduct) > k:
            currentProduct = currentProduct / elem

            tempProducts.append(currentProduct)
            currentProduct = elem

    print(tempProducts)

    return len(tempProducts)




if __name__ == '__main__':
    a = [2,3,3,7,3,5]
    k = 20
    getMinLength(a,k)