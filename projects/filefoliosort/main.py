import os
import shutil
import sys

def validate_directory(directory):
    if not os.path.isdir(directory):
        return False, f'Error: {directory} is not a valid directory.'
    return True, None


def organize_files(source_dir, target_dir):
    try:
        files_moved = 0
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)

            if os.path.isfile(source_path):
                extension = filename.split('.')[-1]
                target_subdirectory = os.path.join(target_dir, extension)

                if not os.path.exists(target_subdirectory):
                    os.makedirs(target_subdirectory)

                target_path = os.path.join(target_subdirectory, filename)
                shutil.move(source_path, target_path)
                files_moved += 1

        return True, f'Successfully moved {files_moved} files.'

    except Exception as e:
        return False, f'An error occurred: {e}'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python main.py <source_directory> <target_directory>')
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    source_valid, source_message = validate_directory(source_directory)
    if not source_valid:
        print(source_message)
        sys.exit(1)

    target_valid, target_message = validate_directory(target_directory)
    if not target_valid:
      print(target_message)
      print("Creating target directory...")
      try:
        os.makedirs(target_directory)
      except OSError as e:
        print(f"Error creating target directory: {e}")
        sys.exit(1)

    success, message = organize_files(source_directory, target_directory)
    print(message)
