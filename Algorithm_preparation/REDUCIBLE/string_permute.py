class PermuteString:
    def permute(self, remaining: str,sofar:str, collected: set) -> int:
        # base case
        if 0 == len(remaining):
            return collected.add(sofar)

        # break string into two parts and swap them
        for i in range(0, len(remaining)):
             #pick one character
            picked_character = remaining[i]
            rest = remaining[0: i] + remaining[i + 1:]
            self.permute(self,rest,sofar + picked_character,collected)

        print(collected)
        return len(collected)

#
# class PermuteString:
#
#     def permute(self,original_input:str,current_counter:int,collected:set)->int:
#         #base case
#         if len(current_counter) == 0 :
#             return 0
#
#         #break string into two parts and swap them
#         for i in range ( 0, len(original_input)):
#             input_first_part = original_input[0:i]
#             input_second_part = original_input[i:]
#             swapped = input_second_part + input_first_part
#             collected.add(swapped)
#             self.permute(self, original_input,, collected)
#
#         return len(collected)

if __name__ == '__main__':
    input = "abc"
    current_counter = 0
    len_input = len(input)
    collector = set()
    print(PermuteString.permute(PermuteString,input,"",collector))
