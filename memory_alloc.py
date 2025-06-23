class MemoryBlock:
    def __init__(self, size: int, start: int):
        self.allocated_size = size
        self.start = start
        self.valid = True

    def __len__(self) -> int:
        return self.current_size
    
    def __eq__(self, other) -> bool:
        if not(isinstance(other, MemoryBlock)):
            return False
        if self.start == other.start and self.allocated_size==other.allocated_size and self.valid == other.valid:
            return True
    
    '''
        Moves memory block start index up (toward zero)

        Params:
            size = number of indices to move up)
        
        Returns:
            None
    '''
    def move_up(self, steps: int):
        self.start -= steps
    
    '''
        Marks the MemoryBlock as deallocated
    '''
    def free(self):
        self.valid=False
        self.start=-1
    
    def __str__(self) -> str:
        return(f'start @ {self.start} size of {self.allocated_size} and {self.valid}')

    
class MemoryManager:
    '''
        Python does not have manual memory alloaction or pointers, so in order to handle allocated space, I use a list that holds chunks of "memory" of various size
        
    '''
    def __init__(self, buffer_size: int):
        self.occupied_space = 0
        self.max_size = buffer_size
        self.contents = []


    '''
        Given a size, allocate a memory chunk to it 

        Params:
            size = size of memory to allocate ("bytes")
        
        Returns:
            MemoryBlock representing the newly created memory chunk

        Raises: 
            MemoryError if not enough memory exists in MemoryManager to create a chunk of the requested size
    '''
    def alloc(self, size: int) -> MemoryBlock:
        if (self.occupied_space+size) > self.max_size:
            raise MemoryError
        else:
            new_mem = MemoryBlock(size, self.occupied_space)
            self.occupied_space+=size
            self.contents.append(new_mem)
            return new_mem
    
    '''
        Given a MemoryBlock object, remove it from the MemoryManager / deallocate its functionality

        Params:
            requested_block = MemoryBlock To Remove
        
        Returns:
            None
        
            Will do nothing if the requested to be removed MemoryBlock is invalid or not in the given 
    '''
    def free(self, requested_block: MemoryBlock): 
        if not(requested_block.valid):
            return
        
        allocated_index = -1
        for index, memory_block in enumerate(self.contents):
            if allocated_index!=-1:
                memory_block.move_up(requested_block.allocated_size)
            elif memory_block==requested_block:
                requested_block.free()
                allocated_index = index
        self.contents.pop(allocated_index)
        self.occupied_space-=requested_block.allocated_size
            

    '''
      Returns String Form of MemoryManager
    '''
    def __str__(self) -> str:
        return_str="{ \n"
        for block in self.contents:
            return_str += str(block) + "\n"
        return_str+="}"
        return return_str
    
    '''
        Returns how much space MemoryManager is occupying
    '''
    def __len__(self) -> int:
        return self.occupied_space
    