import tarfile
import os
import tempfile
import pathlib

def extract_and_read_tar(tar_path, file_to_read):
    """
    Extracts a tar archive to /tmp/unpack and reads a specified file.

    :param tar_path: Path to the tar archive.
    :param file_to_read: Name of the file to read after extraction.
    """
    # Use tempfile module to securely create a temporary directory
    with tempfile.TemporaryDirectory() as extract_path:
        extract_path = pathlib.Path(extract_path)

        def is_safe_path(base_path, path, follow_symlinks=True):
            # Resolve the absolute path
            if follow_symlinks:
                return os.path.realpath(path).startswith(base_path)
            return os.path.abspath(path).startswith(base_path)

        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_safe_path(path, member_path):
                    raise Exception(f"Detected a potentially unsafe path: {member.name}")
                # Ensure member's name doesn't contain components like '..'
                if ".." in member.name or member.name.startswith("/"):
                    raise Exception(f"Detected a potentially unsafe file name: {member.name}")
            tar.extractall(path, members, numeric_owner=numeric_owner)

        # Extract tar file after validating each member
        with tarfile.open(tar_path, 'r:*') as tar:
            safe_extract(tar, path=str(extract_path))  # Ensure path is a string

        # Read a specific file from the extracted contents
        file_path = extract_path / file_to_read
        if file_path.is_file():
            with file_path.open('r') as file:
                content = file.read()
                print(content)
        else:
            print(f"File {file_to_read} not found in the extracted contents.")

# Example usage
# extract_and_read_tar('example.tar.gz', 'example.txt')