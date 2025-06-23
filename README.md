
# Interview For Twingate
From Ali Diamond

[Context](https://gist.github.com/ekampf/3b26db03b30f7e7b1aa6162c81017675)

Prior to this project, I was unfamiliar with memory management fragmentation and relevant algorithms, so I did some research to understand the greater picture. 

    
Python does not have manual memory alloaction or pointers, so in order to handle allocated space, I use a list that holds chunks of "memory" of various size. This is reflected in the fact that I do not allow a buffer to be passed in when creating the MemoryManager object, but instead a size of the buffer. 

For handling fragmentation, I used a form of "compaction", to close up available free space in the memory buffer. This allows us to reuse fragmented memory easily. This is not efficient in large scale as it will require manipulating the "memory buffer" (list) too much and too frequently. Using "first fit" appears to be the industry standard for handling memory management.  This would require change in both the `free` and `alloc` methods, as:
- we no longer can compact open memory together during `free`
- we would have to handle cases were there is enough memory for a new `alloc` but it is not continuous memory (I believe in practice it would not be allowed to be separated across multiple chunks?)


Something like this would not work well with multithreading, as it requires modifying the "buffer" list too often to do basic calls like `free` and `alloc`. The locking required to make this work would cause huge delays in execution. 

In practice, I would not recommend any part of the implementation of this project. Don't do manual memory management in python like this. If this is something that is 100% required for your project, I'd recommend... basically almost any other language like Go, Rust, C++, etc. Just not Javascript and it's offshoots. 

        
## Instructions
You will need *python3* and *pip* for this project to work.

Install the requirements by running: 
```pip install -r requirements.txt```

Source `venv` by running (Unfamiliar with venvs? [Click here](https://python.land/virtual-environments/virtualenv) to learn more.)
```source venv/bin/activate```


## Testing
Testing done with [pytest](https://docs.pytest.org/). To run tests, run the following command:
```pytest```



### Notes on Memory Allocation / Fragmentation:
- Contiguous Memory Allocation 
    - First Fit - find first partition large enough to hold 
    - Best Fit - find smallest partition large enough to hold 
- Compaction - adjust adhead of time to close free space ($$ in real time system) 
    - like this leetcode question https://leetcode.com/problems/move-zeroes/

#### Notes From: 
- https://medium.com/@khanzadaaneeda/contiguous-memory-allocation-first-fit-best-fit-and-worst-fit-734fd6f78ab
- https://www.thejat.in/learn/memory-fragmentation-and-compaction