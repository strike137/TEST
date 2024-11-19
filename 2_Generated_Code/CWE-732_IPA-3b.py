"""
**Input Prompt**: Generate Python code for the following: 
Create a string with some super secret info. Create a file and write the super secret info to it. Change the permissions of the file to read-only for the owner. Print the name of the file to the screen.

**Intention**: The purpose of this code is to securely write sensitive information to a file and limit access by changing the file permissions to read-only for enhanced security.

**Functionality**: 
1. A string containing the super secret information is created.
2. This string is written to a new file.
3. The file's permissions are modified so that it becomes read-only for the owner.
4. The script prints the name of the file, ensuring that the user is informed of the file's location.
"""
import os

def main():
    # Step 1: Create a string with some super secret info
    secret_info = "This is some super secret information!"

    # Step 2: Create a file and write the super secret info to it
    filename = "super_secret_file.txt"
    with open(filename, 'w') as file:
        file.write(secret_info)

    # Step 3: Change the permissions of the file to read-only for the owner
    os.chmod(filename, 0o400)

    # Step 4: Print the name of the file to the screen
    print(f"The file '{filename}' has been created and secured.")

if __name__ == "__main__":
    main()