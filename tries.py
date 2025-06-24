#Prefix tree
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

trie = PrefixTree()
trie.insert("apple")
print(trie.search("apple"))    
print(trie.search("app"))      
print(trie.startsWith("app"))  
trie.insert("app")
print(trie.search("app"))      

#Q2. Word Dictionary
class WordTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = WordTrieNode()

    def addWord(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordTrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

print(wd.search("pad"))   
print(wd.search("bad"))  
print(wd.search(".ad"))   
print(wd.search("b.."))   

