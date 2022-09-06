#https://www.youtube.com/watch?v=5o-kdjv7FD0&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=2

from typing import List


class Solution:
    def ways_to_climb(self, total_stairs: int) -> int:
        #total_valid_emails = []
        unique_domain = set()
        for single_email in emails:
            possible_values = single_email.split('@')
            possible_after_splitting_by_plus = possible_values[0].split("+")
            filtered_mail = possible_after_splitting_by_plus[0].replace(".", "")
            #total_valid_emails.append(filtered_mail)
            final_mail = filtered_mail.join(possible_values[1])
            unique_domain.add(final_mail)
            #extra check should be added for the unique domain names

        return len(unique_domain)


if __name__ == '__main__':
    num_ways = 4

    print(Solution.ways_to_climb(Solution,num_ways))

