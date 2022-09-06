from typing import List




class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # total_valid_emails = []
        unique_domain = set()
        for single_email in emails:
            possible_values = single_email.split('@')
            possible_after_splitting_by_plus = possible_values[0].split("+")
            filtered_mail = possible_after_splitting_by_plus[0].replace(".", "")
            # total_valid_emails.append(filtered_mail)
            final_mail = filtered_mail.join(possible_values[1])
            unique_domain.add(final_mail)
            # extra check should be added for the unique domain names

        return len(unique_domain)

if __name__ == '__main__':
    possible_mails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                      "testemail+david@lee.tcode.com"]

print(Solution.numUniqueEmails(Solution, possible_mails))

