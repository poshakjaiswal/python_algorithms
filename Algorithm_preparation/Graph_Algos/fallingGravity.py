def applyGravity(nums):
    output = []  # contain the tuples that are falling

    failing = set()

    for index in range(len(nums)-1, 0,-1): #row

        for indexCol,element in enumerate(nums[index]):
            if element == 0 :
                failing.add((index,indexCol))


    def collectFallinginColumn(nums,currentFixedColumn):

        for index in range(len(nums) - 1, 0,-1):
            output.append((index,currentFixedColumn ))


    for element in failing:
        collectFallinginColumn(nums,element)


    return  output




nums = [[ 0 ,1 ,0 ,1 ],
[ 1 ,0 ,0 ,1 ],
[ 0 ,0 ,1 ,0 ],
[ 0 ,1 ,0 ,0 ]
]

print(applyGravity(nums))