# Trie Data Structure Implementation

class TrieNode:
    def __init__(self):
        # Each node holds a dictionary of its children and a flag to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Inserts a word into the trie
        node = self.root
        for char in word:
            # If the character isn't a child of the current node, create it
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # After inserting all characters, mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Searches for a complete word in the trie
        node = self.root
        for char in word:
            # If the character isn't found, the word doesn't exist
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True only if it's marked as the end of a word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Checks if any word in the trie starts with the given prefix
        node = self.root
        for char in prefix:
            # If the character isn't found, no word starts with this prefix
            if char not in node.children:
                return False
            node = node.children[char]
        # If we reach here, at least one word starts with the given prefix
        return True


