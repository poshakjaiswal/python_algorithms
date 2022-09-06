class Solution :

    def is_valid_zip(zip_code):
        """Returns whether the input string is a valid (5 digit) zip code
        """
        digit_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        if len(zip_code) == 5:
            for char in zip_code:
                if int(char) not in digit_set:
                    return False
            return True
        return False

    def word_search(doc_list, keyword):
        """
        Takes a list of documents (each document is a string) and a keyword.
        Returns list of the index values into the original list for all documents
        containing the keyword.

        Example:
        doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
        >>> word_search(doc_list, 'casino')
        >>> [0]
        """
        keyword_uppercase = keyword.upper()
        index = 0
        for item in doc_list:
            upper_case = item.upper()
            upper_case = upper_case.replace(".", "")
            sets = set(upper_case.split(" "))

            if keyword_uppercase in sets:
                return [index]
            index = index + 1

        return []


if __name__ == '__main__':
    zip_code = '12345'
    print(Solution.is_valid_zip(zip_code))
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    print(Solution.word_search(doc_list, 'casino'))


