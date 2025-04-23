# Merkle Hash Tree for File Integrity Check

This project uses a Merkle Hash Tree algorithm to verify the integrity of multiple files. It computes a "Top Hash" value that represents the collective integrity of all input files and demonstrates how this hash changes when any file is modified.

## What is a Merkle Tree?

A Merkle Tree (or Hash Tree) is a binary tree data structure where:
- Leaf nodes contain hashes of data blocks (in our case, files)
- Non-leaf nodes contain hashes of their children
- The root node (Top Hash) effectively represents the integrity of all data

This structure is efficient for verifying the integrity of data in distributed systems and is used in various applications including blockchain technology, Git version control, and many file systems.

## Features

- Processes any number of input files (can handle thousands)
- Uses SHA-1 for hashing files
- Builds a complete Merkle Tree and computes the Top Hash
- Demonstrates how modifying any file changes the Top Hash
- Written in Python

## Requirements

- Python 3.6 or higher
- No external dependencies beyond the Python standard library

## Installation

Simply clone the repository:

```bash
git clone https://github.com/andrewshowers/Merkle-Hash-Tree.git
cd merkle-hash-tree
```

## Usage
Run the program with the paths to the files you want to check:

```bash
python merkle_tree.py file1.txt file2.txt file3.txt
```
You can provide any number of file paths as arguments.

## How It Works
1. The program hashes each input file using SHA-1
2. It pairs these hashes and hashes them together to form parent nodes
3. This process continues recursively until a single top hash is obtained
4. The program then demonstrates how modifying a file changes the top hash

## Example Output

```Powershell
Processing 2 files...
Hash for .\test.txt: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
Hash for .\test2.txt: 109f4b3c50d7b0df729d299bc6f8e9ef9066971f

Top Hash: 51e109ace2542940f37aeb40632644f4a9bea357

Demonstrating modification detection using .\test.txt...
Original Top Hash: 51e109ace2542940f37aeb40632644f4a9bea357
Modified Top Hash: 35a506507aa1614356af40e411b71fb68f73de1b
Hashes match: False
Restored original content of .\test.txt
```
