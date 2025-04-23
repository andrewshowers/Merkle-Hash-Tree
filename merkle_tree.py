import hashlib
import sys

def hash_file(file_path):
    """Calculate SHA-1 hash of a file"""
    hasher = hashlib.sha1()
    
    with open(file_path, 'rb') as f:
        # Read in chunks to handle large files
        chunk = f.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(4096)
            
    return hasher.hexdigest()

def build_merkle_tree(file_hashes):
    """Build merkle tree from hashes and return the top hash"""
    # If there's only one hash, it's the top hash
    if len(file_hashes) == 1:
        return file_hashes[0]
    
    # Create pairs of hashes
    next_level = []
    for i in range(0, len(file_hashes), 2):
        # If we have a pair, hash them together
        if i + 1 < len(file_hashes):
            combined = file_hashes[i] + file_hashes[i + 1]
        # If odd number, duplicate the last one
        else:
            combined = file_hashes[i] + file_hashes[i]
            
        # Hash the combined value
        hasher = hashlib.sha1()
        hasher.update(combined.encode('utf-8'))
        next_level.append(hasher.hexdigest())
    
    # Recursively build the tree until we get the top hash
    return build_merkle_tree(next_level)

def main():
    # Get file paths from command line arguments
    if len(sys.argv) < 2:
        print("Usage: python merkle_tree.py <file1> <file2> ... <fileN>")
        return
        
    file_paths = sys.argv[1:]
    print(f"Processing {len(file_paths)} files...")
    
    # Calculate hash for each file
    file_hashes = []
    for file_path in file_paths:
        try:
            file_hash = hash_file(file_path)
            file_hashes.append(file_hash)
            print(f"Hash for {file_path}: {file_hash}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Build the Merkle tree and get the top hash
    top_hash = build_merkle_tree(file_hashes)
    print(f"\nTop Hash: {top_hash}")
    
    # Prove modification detection
    if file_paths:
        test_file = file_paths[0]
        print(f"\nDemonstrating modification detection using {test_file}...")
        
        # Save original content
        with open(test_file, 'rb') as f:
            original_content = f.read()
        
        try:
            # Modify the file
            with open(test_file, 'ab') as f:
                f.write(b"\nThis file was modified")
            
            # Recalculate hashes
            modified_hashes = []
            for file_path in file_paths:
                modified_hashes.append(hash_file(file_path))
            
            # Get new top hash
            new_top_hash = build_merkle_tree(modified_hashes)
            
            # Compare hashes
            print(f"Original Top Hash: {top_hash}")
            print(f"Modified Top Hash: {new_top_hash}")
            print(f"Hashes match: {top_hash == new_top_hash}")
            
        finally:
            # Restore the original file
            with open(test_file, 'wb') as f:
                f.write(original_content)
            print(f"Restored original content of {test_file}")

if __name__ == "__main__":
    main()