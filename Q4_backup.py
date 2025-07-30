import os                  # For file and directory path operations
import shutil              # For copying files
import sys                 # For reading command-line arguments
from datetime import datetime  # For generating timestamps

def backup_files(src, dst):
    """
    Copies files from a source directory to a destination directory.
    If a file with the same name already exists in the destination,
    a timestamp is appended to the filename to ensure uniqueness.

    Parameters:
        src (str): Source directory path
        dst (str): Destination directory path
    """
    
    # Check if the source directory exists
    if not os.path.exists(src):
        print(f"❌ Source directory '{src}' does not exist.")
        return

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Iterate over each file in the source directory
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dst_path = os.path.join(dst, filename)

        # Proceed only if the current item is a file (ignore directories)
        if os.path.isfile(src_path):
            # If file with same name exists in destination, append timestamp
            if os.path.exists(dst_path):
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dst_path = os.path.join(dst, f"{base}_{timestamp}{ext}")

            # Copy file from source to destination
            shutil.copy2(src_path, dst_path)
            print(f"✅ Backed up: {filename} ➡ {dst_path}")

if __name__ == "__main__":
    # Check if the user provided the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
    else:
        # Execute the backup function with provided source and destination
        backup_files(sys.argv[1], sys.argv[2])
