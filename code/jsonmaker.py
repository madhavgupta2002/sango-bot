import os
import json

def process_folder(folder_path):
    # Create output JSON file path
    json_filename = f"{os.path.basename(folder_path)}_transcripts.json"
    json_filepath = os.path.join(folder_path, json_filename)
    
    transcripts = []
    
    # Process each txt file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # Get title without extension
            title = os.path.splitext(filename)[0]
            
            # Read content from file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            # Add to transcripts list
            transcripts.append({
                'title': title,
                'content': content
            })
    
    # Write JSON file
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(transcripts, f, indent=2, ensure_ascii=False)

def main():
    # Get all folders in current directory
    current_dir = os.getcwd()
    folders = [f for f in os.listdir(current_dir) 
              if os.path.isdir(os.path.join(current_dir, f))]
    
    # Process each folder
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        process_folder(folder_path)

if __name__ == '__main__':
    main()
