"""
**Input Prompt**: Generate Python code for the following: The code allocates two chunks of memory. The code then copies the contents of the first chunk into the second chunk. The code then prints the contents of the second chunk. The code then frees the memory allocated to the first chunk. The code then prints the contents of the second chunk. The code then frees the memory allocated to the second chunk.

**Intention**: The purpose of this code is to demonstrate memory allocation, copying of contents between allocations, and deallocation in Python using lists as an analogy for demonstrating the concept of memory manipulation.

**Functionality**: The code initializes two lists to simulate memory allocation, copies the content of the first list into the second list, 
prints the content of the second list, clears the first list to simulate freeing memory, prints the content of the second list again to 
show persistence of copied contents, and finally clears the second list to demonstrate complete deallocation.
"""
def memory_simulation():
    """Simulate memory operations with lists."""
    # Simulate allocating memory chunks as lists
    first_chunk = [1, 2, 3, 4, 5]
    second_chunk = [0] * len(first_chunk)
    
    # Copy the contents of the first chunk into the second chunk
    second_chunk = first_chunk[:]
    
    # Print the contents of the second chunk
    print("Second chunk after copying:", second_chunk)
    
    # Free the memory allocated to the first chunk
    first_chunk.clear()
    
    # Print the contents of the second chunk after freeing the first
    print("Second chunk after freeing first chunk:", second_chunk)
    
    # Free the memory allocated to the second chunk
    second_chunk.clear()

if __name__ == "__main__":
    memory_simulation()