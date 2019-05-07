class MemorySystem:
    def __init__(self, max_size=5):
        # Doubly linked list representation
        self._key = [None] * max_size
        self._next_idx = [None] * max_size  
        
        # Pointer to first free memory page index
        self._free = 0
        for i in range(1, max_size):
            self._next_idx[i-1] = i
    
    def allocate(self, obj):
        if self._free is None:
            raise ValueError("Out of space")
        
        allocated_idx = self._free
        self._key[allocated_idx] = obj 
        self._free = self._next_idx[allocated_idx]
        
        return allocated_idx
    
    def deallocate(self, obj_idx):
        self._key[obj_idx] = None
        self._next_idx[obj_idx] = self._free
        self._free = obj_idx

        # Keep list of free pages sorted for compact representation
        pages = []
        
        idx = self._free
        while idx is not None:
            pages.append(idx)
            idx = self._next_idx[idx]
        
        pages = sorted(pages)

        # Recreate free-list
        self._free = pages[0]
        
        for i in range(1, len(pages)):
            self._next_idx[pages[i-1]] = pages[i]
        
        self._next_idx[pages[-1]] = None


if __name__ == "__main__":
    test = MemorySystem()
    for i in range(5):
       print(test.allocate(i))
    test.deallocate(0)
    test.deallocate(3)
    test.deallocate(4)
    print(test.allocate(111))
    test.deallocate(2)
    test.deallocate(1)
    test.deallocate(0)
    for i in range(5):
       print(test.allocate(i))