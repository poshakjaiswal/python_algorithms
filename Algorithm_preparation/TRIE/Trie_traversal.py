class TrieNode:
    def __init__(self):
        self.isWord = False
        self.nodes = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        cur = self.root;
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
        cur.isWord = True;

    # Returns if the word is in the trie
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return cur.isWord

    # Returns if there is any word in the trie that starts with the given prefix. */
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        return True


trie = Trie()
dictionary = ["pirate", "king", "leetcode", "cheat", "sheet"]
for word in dictionary:
    trie.insert(word)

print("=== check whether words exist in the trie ===")
searchWords = ["pirate", "king", "leetcode", "cheat", "sheet", "abc", "apple", "faang", "google"]
for word in searchWords:
    print(word + " exists: " + str(trie.search(word)))

print("=== check if there's any word that starts with the given prefix in the trie ===")

startsWithWords = ["p", "kin", "leet", "cheeze", "shell", "faang"]
for prefix in startsWithWords:
    print("prefix " + prefix + ": " + str(trie.startsWith(prefix)))