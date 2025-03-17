# Dedupy

## Description:
The Deduplicator is a Python utility that helps you identify and handle duplicate files within a directory. It can hash files using several algorithms, such as xxhash, blake3, or sha256, and offers several strategies for handling duplicates, including creating hard links, deleting duplicates, or renaming them. The tool can process files in parallel using multiple threads and supports exclusion patterns to skip specific files from processing.

## Installation:
1. Install the required Python libraries using pip:
   `pip install pybloom-live tqdm mmappickle`

2. If you want to use the `xxhash` or `blake3` hashing algorithms, install the optional libraries:
   pip install xxhash blake3

3. Installing the package
   `python setup.py install`

## Usage:
You can run the deduplication process by executing the Python script with the required arguments.

### Command Syntax:
```
python deduplicator.py <directory> [options]

Arguments:
  <directory>            Directory to scan for duplicates.
  --hash-file <file>     File to store hashes (default: .hashes.db).
  --buffer-size <size>   Buffer size for hashing (default: 65536, 64KB).
  --hash-algorithm <alg> Hashing algorithm to use (choices: "xxhash", "blake3", "sha256", default: "xxhash" if available).
  --replace-strategy <strategy> Strategy for handling duplicates (choices: "hardlink", "delete", "rename", default: "hardlink").
  --max-threads <num>    Number of threads to use for processing (default: 4).
  --sync-interval <num>  Sync interval for hashes to disk (default: 100).
  --progress             Show a progress bar while processing files.
  --dry-run              Simulate the deduplication process without making any changes.
```

## Features:
1. **Hash Algorithms**: Choose between `xxhash`, `blake3`, and `sha256` for calculating file hashes.
2. **Duplicate Handling Strategies**: 
   - `hardlink`: Replace duplicates with hard links.
   - `delete`: Delete duplicate files.
   - `rename`: Rename duplicate files by appending `.duplicate` to their names.
3. **Multi-threading**: Process files in parallel to speed up deduplication.
4. **Bloom Filter**: Optionally, enable the Bloom filter to speed up duplicate checks by avoiding re-hashing files.
5. **Exclusion Patterns**: Exclude files matching specific patterns from the deduplication process.
6. **Progress Bar**: Optionally display a progress bar for better visibility during the deduplication process.
7. **Dry Run**: Run the deduplication process without making any actual changes (useful for testing).

## Class Details:
Deduplicator:
  - `__init__(self, directory, hash_file, buffer_size, hash_algorithm, replace_strategy, max_threads, sync_interval, progress, dry_run, exclude_patterns, use_bloom_filter=False)`:
    Initializes the Deduplicator class with the necessary parameters.
  - `count_files(directory)`:
    Counts the number of files in the given directory.
  - `_mmap_hashes_file()`:
    Loads or creates an mmapdict for storing file hashes.
  - `_load_bloom_filter()`:
    Loads existing hashes into a Bloom filter for faster lookups.
  - `get_file_hash(file_path)`:
    Calculates and returns the hash of a file using the selected hashing algorithm.
  - `are_same_file(file1, file2)`:
    Checks if two files are the same based on their inodes.
  - `create_hard_link(source, target)`:
    Creates a hard link from the source file to the target file.
  - `delete_duplicate(file_path)`:
    Deletes a duplicate file.
  - `rename_duplicate(file_path)`:
    Renames a duplicate file by appending `.duplicate`.
  - `is_excluded(file_path)`:
    Checks if a file matches any exclusion pattern.
  - `add_file_hash_database(file_hash, file_path)`:
    Adds a file hash to the database and syncs the data periodically.
  - `process_file(file_path)`:
    Processes a single file to check for duplicates and handles them according to the specified strategy.
  - `deduplicate()`:
    Scans the directory for duplicates and processes each file.
  - `print_stats()`:
    Prints the deduplication statistics (total files processed, duplicates found, duplicates removed, hard links created, space saved).

## Example Usage:
1. **Basic deduplication (using default hashing algorithm)**:
   `python deduplicator.py /path/to/directory`

2. **Using SHA256 as the hashing algorithm**:
   `python deduplicator.py /path/to/directory --hash-algorithm sha256`

3. **Using a custom hash file and buffer size**:
   `python deduplicator.py /path/to/directory --hash-file .custom_hashes.db --buffer-size 131072`

4. **Simulate deduplication (dry run)**:
   `python deduplicator.py /path/to/directory --dry-run`

5. **Create hard links for duplicates, use Bloom filter, and show progress**:
   `python deduplicator.py /path/to/directory --replace-strategy hardlink --use-bloom-filter --progress`

## Logging:
Logging is set up to provide debug-level output. You can adjust the logging level by modifying the `logging.basicConfig()` call or setting it via command line options. Logs include:
- Hashing algorithm used.
- Files being processed.
- Details of duplicates found and the actions taken (hard link creation, deletion, renaming).
- Sync status for hash file.

## Stats:
After deduplication, the following statistics are shown:
- Total files processed.
- Duplicate files found.
- Duplicates removed.
- Hard links created.
- Total space saved (in MB).

## Dependencies:
- pybloom-live: A library for Bloom filter implementation.
- tqdm: For showing a progress bar.
- mmappickle: For memory-mapped hash storage.
- xxhash (optional): For faster hashing if available.
- blake3 (optional): For faster hashing if available.

## License:
This software is distributed under the MIT License.
```bash
python src/main.py /path/to/directory --hash-algorithm xxhash --replace-strategy hardlink --progress --use-bloom-filter


