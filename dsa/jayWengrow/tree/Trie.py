class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        return currentNode

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children['*'] = None

    def collectAllWords(self, node=None, word="", words=[]):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)

    def traverse(self, node=None):
        """a function that traverses each node of a trie and prints
         each key, including all "*" keys."""
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverse(childNode)

    def autocorrect(self, word):
        """
        function that attempts to replace a user's typo with a correct word.
        This function accepts a string that represents text a user typed in.
        If the user's string is not in the trie, the function should return an
        alternative word that shares the longest possible prefix with the
        user's string.
        """
        currentNode = self.root
        wordFoundSoFar = ""
        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char
                currentNode = currentNode.children.get(char)
            else:
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]
        return word
