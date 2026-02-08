import os
import sys

def organize_files(directory):
    """Organizes files in a directory by extension."""
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    files_moved = 0
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = filename.split('.')[-1].lower() if '.' in filename else 'uncategorized'
            
            if extension == filename:
                extension = 'uncategorized'

            extension_dir = os.path.join(directory, extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(extension_dir, filename)

            try:
                os.rename(old_path, new_path)
                files_moved += 1
                print(f"Moved '{filename}' to '{extension_dir}'")
            except FileExistsError:
                print(f"Warning: File '{filename}' already exists in '{extension_dir}'. Skipping.")
            except Exception as e:
                print(f"Error moving '{filename}': {e}")
    
    print(f"Organized {files_moved} files in '{directory}'.")


def validate_path(path):
    """Validates that the given path exists."""
    if not os.path.exists(path):
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        if not validate_path(directory_path):
            print(f"Error: Invalid directory path: {directory_path}")
        else:
            organize_files(directory_path)
    else:
        organize_files(os.getcwd())
