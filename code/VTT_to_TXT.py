import os
import re

def clean_vtt_text(text):
    # Remove timestamp lines (00:00:00.000 --> 00:00:00.000)
    text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*\n', '', text)
    
    # Remove WebVTT header
    text = re.sub(r'WEBVTT\nKind:.*\nLanguage:.*\n', '', text)
    
    # Remove timestamp tags (<00:00:00.000>)
    text = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}>', '', text)
    
    # Remove style tags (<c> and </c>)
    text = re.sub(r'</?c>', '', text)
    
    # Remove empty lines and position markers
    text = re.sub(r'\n\s*\n', '\n', text)
    text = re.sub(r'align:.*position:.*%\n', '', text)
    
    # Clean up any remaining whitespace
    text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\s+$', '', text, flags=re.MULTILINE)
    
    # Remove duplicate consecutive lines
    lines = text.split('\n')
    unique_lines = []
    prev_line = None
    for line in lines:
        if line != prev_line and line.strip():
            unique_lines.append(line)
        prev_line = line
    
    # Join lines with spaces instead of newlines
    return ' '.join(unique_lines).strip()

def convert_vtt_files():
    # Create converted directory if it doesn't exist
    if not os.path.exists('converted'):
        os.makedirs('converted')
    
    # Process all .vtt files in current directory
    for filename in os.listdir('.'):
        if filename.endswith('.vtt'):
            with open(filename, 'r', encoding='utf-8') as f:
                vtt_content = f.read()
            
            # Clean the text
            clean_text = clean_vtt_text(vtt_content)
            
            # Create output filename
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_path = os.path.join('converted', output_filename)
            
            # Write cleaned text to output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(clean_text)

if __name__ == '__main__':
    convert_vtt_files()

