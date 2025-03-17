# File Deduplication Tool

This Python script identifies and handles duplicate files in a specified directory. It supports multiple hashing algorithms, duplicate handling strategies, and performance optimizations like Bloom filters and multithreading.

---

## Features

### 1. **Hashing Algorithms**
   - Supports `xxhash`, `blake3`, and `sha256` for file comparison.
   - Automatically selects the fastest available algorithm (`xxhash` > `blake3` > `sha256`).

### 2. **Duplicate Handling Strategies**
   - **Hardlink**: Replace duplicates with hard links to save space.
   - **Delete**: Remove duplicate files.
   - **Rename**: Append `.duplicate` to the filename of duplicates.

### 3. **Performance Optimizations**
   - **Bloom Filter**: Optionally uses a Bloom filter to speed up duplicate checks.
   - **Multithreading**: Processes files concurrently using a thread pool.
   - **Memory-Mapped Hash Storage**: Uses `mmappickle` to store file hashes efficiently.

### 4. **Exclusion Patterns**
   - Exclude files matching specific patterns (e.g., `*.tmp`, `backup/*`).

### 5. **Dry Run Mode**
   - Simulates the deduplication process without making any changes.

### 6. **Progress Tracking**
   - Displays a progress bar using `tqdm` when enabled.

### 7. **Statistics**
   - Tracks and reports deduplication statistics, including space saved and duplicates removed.

---

## Usage

Run the script from the command line with the desired arguments:

```bash
python src/main.py /path/to/directory --hash-algorithm xxhash --replace-strategy hardlink --progress --use-bloom-filter


