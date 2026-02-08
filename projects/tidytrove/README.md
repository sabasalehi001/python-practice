# TidyTrove

TidyTrove is a simple command-line tool to organize files in a directory based on their file extension. It creates subdirectories for each extension type and moves the corresponding files into them.

## Usage

```
python main.py <directory_path>
```

Replace `<directory_path>` with the path to the directory you want to organize.  If no path is provided, the current directory will be used.

## Example

```
python main.py /path/to/my/files
```

This will create subdirectories like `txt`, `pdf`, `jpg`, etc., within `/path/to/my/files` and move the appropriate files into them.
