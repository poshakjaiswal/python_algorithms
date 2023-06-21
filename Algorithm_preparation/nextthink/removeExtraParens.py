
def removeUnbalancingParens( input ):

    output = input

    stack = []

    validParensMap = dict()

    validParensMap['('] = ')'

    def isNullyfyingPrevious(Currentchar,index):

        #previous indexes in arraymap

        if   len(stack)> 0 and     arrayMap[len(arrayMap) -1 ] ==



    for index,char in  enumerate(input):

        if isNullyfyingPrevious(char,index):
            #remove the occurence with balancing index
            stack.pop() # index it was matching



        else:

            stack.append(char,index)



    for item in   arrayMap:

        #remove the element from input







    return output






input = "ab(a(c)fg)9)"
print(removeUnbalancingParens(input))

#unit test cases


