from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1 

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        def is_better(i: int, j: int) -> bool:
            if j == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return True
            if len(wordsContainer[i]) == len(wordsContainer[j]) and i < j:
                return True
            return False

        global_best = 0
        for i in range(1, len(wordsContainer)):
            if is_better(i, global_best):
                global_best = i
        root.best_index = global_best

        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                if is_better(i, curr.best_index):
                    curr.best_index = i

        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_index)
            
        return ans