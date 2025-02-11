import csv
import subprocess
import sys
import os

# Check command line arguments
if len(sys.argv) < 3:
    print("Usage: python tag_lightnovels.py <csv_file> <tag>")
    sys.exit(1)

csv_file = sys.argv[1]
new_tag = sys.argv[2]

# Get Calibre library path from environment variable or use default
calibre_library = os.getenv('CALIBRE_LIBRARY', '/books/Calibre_Library')

# Function to check if the tag exists in current tags
def tag_exists(metadata, tag):
    for line in metadata.splitlines():
        if line.startswith('Tags'):
            existing_tags = line.split(':', 1)[1].strip().split(', ')
            return tag in existing_tags
    return False

# Function to append new tag to existing tags
def append_tag(metadata, tag):
    for line in metadata.splitlines():
        if line.startswith('Tags'):
            existing_tags = line.split(':', 1)[1].strip().split(', ')
            existing_tags.append(tag)
            return ', '.join(sorted(set(existing_tags)))
    return tag

# Read CSV and process each book
with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        book_id = row['id']
        try:
            result = subprocess.run([
                'calibredb', '--with-library', calibre_library, 'show_metadata', str(book_id)
            ], capture_output=True, text=True, check=True)

            if not tag_exists(result.stdout, new_tag):
                updated_tags = append_tag(result.stdout, new_tag)
                subprocess.run([
                    'calibredb', '--with-library', calibre_library, 'set_metadata', str(book_id), 
                    '--field', f'tags:{updated_tags}'
                ], check=True)
                print(f'Added tag "{new_tag}" to book with ID {book_id}')
            else:
                print(f'Book with ID {book_id} already has the tag "{new_tag}".')
        
        except subprocess.CalledProcessError as e:
            print(f'Failed to process book with ID {book_id}: {e}')

print("Tagging complete.")
