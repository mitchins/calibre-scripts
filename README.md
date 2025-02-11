# calibre-scripts

This repository contains scripts to manage and tag books in a Calibre library.

## Scripts

### `tag_books.py`

This script is used to tag books in your Calibre library based on a CSV file.

#### Usage

```sh
python tag_books.py <csv_file> <tag>
```

# calibre-scripts
<csv_file>: Path to the CSV file containing book IDs.
<tag>: The tag to be added to the books.
Example
This command will add the tag "Science Fiction" to all books listed in books.csv.

Requirements
Python 3.x
Calibre installed and calibredb command available in your PATH.
Environment variable CALIBRE_LIBRARY set to the path of your Calibre library or use the default /books/Calibre_Library.
CSV File Format
The CSV file should have a header row with at least one column named id which contains the book IDs.

Environment Variables
CALIBRE_LIBRARY: Path to your Calibre library. If not set, the default /books/Calibre_Library will be used.
License
This project is licensed under the MIT License. See the LICENSE file for details.