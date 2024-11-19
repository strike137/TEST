"""
**Input Prompt**: 
Generate Python code for the following: 
The code allocates a buffer of size buffer_size.Then it frees the buffer in a loop.

**Intention**:
The purpose of this code is to demonstrate a simple memory allocation and deallocation process in Python, simulating manual memory management in languages like C/C++ where memory is manually allocated and freed.

**Functionality**:
The code defines a function to allocate a buffer of a given size using a bytearray, which simulates a block of memory. It then runs a loop to 'free' (delete) this buffer and recreate it multiple times, simulating a basic manual memory allocation and deallocation mechanism in a controlled loop, while printing the status to show the process.
"""
def allocate_and_free_buffer(buffer_size, repeat=3):
    """
    Allocates a buffer of the specified size and 'frees' it repeatedly.

    Parameters:
    buffer_size (int): Size of the buffer to allocate.
    repeat (int): Number of times to allocate and free the buffer.
    """
    for i in range(repeat):
        buffer = bytearray(buffer_size)
        print(f"Buffer of size {buffer_size} allocated.")
        del buffer
        print(f"Buffer freed {i + 1} times.")

# Example usage
if __name__ == "__main__":
    buffer_size = 1024  # Example buffer size
    allocate_and_free_buffer(buffer_size, repeat=3)