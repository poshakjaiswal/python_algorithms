class Solution:

    def reduceToInt(self, num: int,index,vals,keyVal, s: str) -> str:

        if num == 0:
            return s


        for i in range ( index,len(vals)) :

            val = vals[i]

            collected = num % val
           # num = num - collected

            # if val == 1:
            #     s = s + "I"


            if collected < num:
                s  = s + keyVal[val]
                return self.reduceToInt(self,num-val,i,vals,keyVal,s)

        return s

    def intToRoman(self, num: int) -> str:

        keyVal = dict()

        keyVal[1] = "I"
        keyVal[5] = "V"
        keyVal[10] = "X"
        keyVal[50] = "L"
        keyVal[100] = "C"
        keyVal[500] = "D"
        keyVal[1000] = "M"

        vals = sorted(list(keyVal),reverse=True)

        return self.reduceToInt(self,num,0, vals,keyVal, "")


if __name__ == "__main__":
    print(Solution.intToRoman(Solution,1994))
