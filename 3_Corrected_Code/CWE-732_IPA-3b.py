import os
import sys

def main():
    # Step 1: Create a string with some super secret info
    secret_info = os.getenv('SUPER_SECRET_INFO')
    if not secret_info:
        print("Error: Sensitive information not provided. Set the environment variable 'SUPER_SECRET_INFO'.")
        sys.exit(1)
    
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