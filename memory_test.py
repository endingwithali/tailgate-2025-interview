from memory_alloc import MemoryManager 
import pytest

'''
Test that is given in example from Tailgate
'''
def test_provided():
    # init buff of 5 chars
    mm = MemoryManager(5)

    # allocate 5 blocks of 1 char each 
    mc1 = mm.alloc(1)
    mc1.give_name("mc1")
    mc2 = mm.alloc(1)
    mc2.give_name("mc2")
    mc3 = mm.alloc(1)
    mc3.give_name("mc3")
    mc4 = mm.alloc(1)
    mc4.give_name("mc4")
    mc5 = mm.alloc(1)
    mc5.give_name("mc5")
    
    
    # free 2nd and 4th 
    mm.free(mc2)
    
    mm.free(mc4) 
    print(mm)


    # call alloc of size 2 (fragmenting code example)
    mc6 = mm.alloc(2)
    print(mm)
    assert len(mm) == 5


'''
Test allocating when
1) allocating less than avail memory
2) filling up avail memory
'''
def test_allocate_less_and_fill():
    # init buff of 2 bytes
    mm = MemoryManager(2)

    # allocate 2 blocks of 1 char each 
    mc1 = mm.alloc(1)
    mc2 = mm.alloc(1)

    assert len(mm) == 2   

'''
Test trying to allocate more memory than available
'''
def test_allocate_larger():
    with pytest.raises(MemoryError):
        mm = MemoryManager(2)
        _ = mm.alloc(6)

'''
Test allocating when
1) allocating less than avail memory
2) attempt to allocate more than available
'''
def test_allocate_and_then_overfill():
    # init buff of 2 bytes
    mm = MemoryManager(2)

    try:
        # allocate 2 blocks of 1 char each 
        mc1 = mm.alloc(1)
        mc2 = mm.alloc(3)
    except MemoryError:
        assert len(mm) == 1   



'''
Test allocating when
1) allocating less than avail memory
2) dealloacte less than avail memory, in order of allocation
'''
def test_allocate_and_free_inorder():
    mm = MemoryManager(4)

    mc1 = mm.alloc(1)
    mc2 = mm.alloc(1)

    mm.free(mc2)
    assert len(mm) == 1

    mm.free(mc1)
    assert len(mm) == 0



'''
Test allocating when
1) allocating less than avail memory
2) dealloacte already deallocated memory
'''
def test_allocate_and_free_already_removed():
    mm = MemoryManager(4)

    mc1 = mm.alloc(1)
    mc2 = mm.alloc(1)

    mm.free(mc2)
    assert len(mm) == 1

    mm.free(mc2)
    assert len(mm) == 1
    
    print(mc1)
