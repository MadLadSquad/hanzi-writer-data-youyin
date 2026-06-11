#!/usr/bin/env python3
import os
import json

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

    # Save the resulting array to character-map-full.json in minified format
    output_full_filename = "character-map-full.json"
    with open(output_full_filename, "w", encoding="utf-8") as f:
        json.dump(full_data, f, ensure_ascii=False, separators=(",", ":"))

if __name__ == "__main__":
    main()
