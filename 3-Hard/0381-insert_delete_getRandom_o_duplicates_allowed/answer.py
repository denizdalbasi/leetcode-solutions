import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        # If val is not present, this will be true
        not_present = len(self.idx_map[val]) == 0
        
        # Add to the list and record its index in the set
        self.idx_map[val].add(len(self.lst))
        self.lst.append(val)
        
        return not_present

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        
        # Get an arbitrary index of 'val' from our set
        remove_idx = self.idx_map[val].pop()
        last_val = self.lst[-1]
        
        # Swap the element to remove with the last element
        self.lst[remove_idx] = last_val
        
        # Add the new index for the swapped element
        self.idx_map[last_val].add(remove_idx)
        # Remove the old index of the swapped element
        self.idx_map[last_val].discard(len(self.lst) - 1)
        
        # Remove the last element from the list
        self.lst.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)