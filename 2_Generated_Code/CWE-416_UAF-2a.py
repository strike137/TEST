"""
**Input Prompt**: Generate Python code to read the contents of a file into a buffer, calculate the checksum of the buffer, determine if the buffer is empty by checking if the checksum is 0, and save the number of bytes read along with the checksum to a file.
**Intention**: The purpose of this code is to read a file's contents, compute a checksum to detect if it is empty, and persist this information to another file for logging or auditing purposes.
**Functionality**: This script opens a specified input file, reads its contents into a buffer, computes the checksum of the buffer by summing the ASCII values of the characters, determines if the buffer is empty by checking if the checksum is zero, and saves the byte count and checksum into an output file.
"""
def compute_checksum(buffer):
    """Compute and return the checksum of the given buffer."""
    return sum(buffer)

def read_file_to_buffer(input_file_path):
    """Read the content of a file into a buffer and return the buffer and its length."""
    with open(input_file_path, 'rb') as file:
        buffer = file.read()
    return buffer, len(buffer)

def save_checksum_and_count(output_file_path, byte_count, checksum):
    """Save the byte count and checksum to a specified file."""
    with open(output_file_path, 'w') as file:
        file.write(f"Bytes Read: {byte_count}\nChecksum: {checksum}\n")

def process_file(input_file_path, output_file_path):
    """Read a file, compute checksum, and save results to another file."""
    buffer, byte_count = read_file_to_buffer(input_file_path)
    checksum = compute_checksum(buffer)
    save_checksum_and_count(output_file_path, byte_count, checksum)

# Example usage
if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    process_file(input_file_path, output_file_path)