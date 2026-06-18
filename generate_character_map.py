#!/usr/bin/env python3
import os
import json
import shutil
import hashlib

def main():
    data_dir = "data"
    if not os.path.exists(data_dir):
        print(f"Error: '{data_dir}' directory does not exist.")
        exit(1)

    # Get all json files and strip their suffix
    files = sorted([
        f[:-5]
        for f in os.listdir(data_dir)
        if os.path.isfile(os.path.join(data_dir, f)) and f.endswith(".json")
    ])

    # Save the resulting array to character-map.json
    output_filename = "character-map.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False)

    # Compile character-map-full data
    full_data = []
    for char_name in files:
        char_file_path = os.path.join(data_dir, f"{char_name}.json")
        with open(char_file_path, "r", encoding="utf-8") as char_file:
            content = json.load(char_file)
        full_data.append({
            "char": char_name,
            "content": content
        })

    # Remove the old character-map-full.json file if it exists
    old_full_filename = "character-map-full.json"
    if os.path.exists(old_full_filename):
        try:
            os.remove(old_full_filename)
        except Exception as e:
            print(f"Warning: Could not remove {old_full_filename}: {e}")

    # Prepare chunks directory
    chunks_dir = "character-map-chunks"
    if os.path.exists(chunks_dir):
        try:
            shutil.rmtree(chunks_dir)
        except Exception as e:
            print(f"Warning: Could not remove existing directory {chunks_dir}: {e}")
    os.makedirs(chunks_dir, exist_ok=True)

    # Partition full_data into chunks of around 1MB in size (1,000,000 bytes)
    # We serialize elements using minified JSON (separators=(',', ':')) to compute size.
    chunks = []
    current_chunk = []
    current_chunk_size = 2  # '[]'
    
    for item in full_data:
        item_str = json.dumps(item, ensure_ascii=False, separators=(",", ":"))
        item_bytes = item_str.encode("utf-8")
        item_size = len(item_bytes)
        
        # calculate size if we add this item
        added_size = item_size + (1 if current_chunk else 0)
        
        # If adding this item would make the chunk exceed 1,000,000 bytes, start a new chunk.
        if current_chunk and current_chunk_size + added_size > 1000000:
            chunks.append(current_chunk)
            current_chunk = [item]
            current_chunk_size = 2 + item_size
        else:
            current_chunk.append(item)
            current_chunk_size += added_size

    if current_chunk:
        chunks.append(current_chunk)

    # Write each chunk to its file in the character-map-chunks directory
    hashes = []
    for i, chunk in enumerate(chunks):
        chunk_filename = os.path.join(chunks_dir, f"character-map-full-{i}.json")
        chunk_content = json.dumps(chunk, ensure_ascii=False, separators=(",", ":"))
        
        # Calculate SHA-256 hash of the chunk file contents
        chunk_hash = hashlib.sha256(chunk_content.encode("utf-8")).hexdigest()
        hashes.append(chunk_hash)
        
        with open(chunk_filename, "w", encoding="utf-8") as f:
            f.write(chunk_content)

    # Save the total number of chunks and their hashes to character-map-chunks.json
    chunks_count_filename = "character-map-chunks.json"
    with open(chunks_count_filename, "w", encoding="utf-8") as f:
        json.dump({"num": len(chunks), "version": hashes}, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
