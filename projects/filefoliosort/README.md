# FileFolioSort

A simple command-line tool to organize files in a directory based on their file extension.

## Usage

```bash
python main.py <source_directory> <target_directory>
```

*   `<source_directory>`: The directory containing the files to be organized.
*   `<target_directory>`: The directory where the organized files will be placed. Subdirectories will be created within this directory based on file extension.

## Example

```bash
python main.py /path/to/unsorted/files /path/to/sorted/files
```

This will create subdirectories in `/path/to/sorted/files` for each file extension found in `/path/to/unsorted/files` and move the corresponding files into those subdirectories.
