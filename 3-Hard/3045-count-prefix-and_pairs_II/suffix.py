from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        root = TrieNode()
        ans = 0
        
        for w in words:
            curr = root
            n = len(w)
            for i in range(n):
                pair = (w[i], w[n - 1 - i])
                if pair not in curr.children:
                    curr.children[pair] = TrieNode()
                curr = curr.children[pair]
                ans += curr.count
            curr.count += 1
            
        return ans