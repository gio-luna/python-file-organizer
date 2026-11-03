# File Organizer

A lightweight Python utility that organizes files into category folders based on their file extensions.

## Requirements

- Python 3

## Usage

Run the script:

```bash
python3 organizer.py
```

When prompted, enter the path to the folder you want to organize. The script processes files in that folder only; it does not scan subfolders.

## Categories

- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`
- Documents: `.pdf`, `.docx`, `.txt`, `.odt`, `.xlsx`, `.pptx`, `.csv`
- Archives: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- Videos: `.mp4`, `.mkv`, `.avi`, `.mov`
- Audio: `.mp3`, `.wav`, `.flac`
- Code: `.py`, `.js`, `.html`, `.css`, `.cpp`, `.c`, `.java`
- Other file extensions are placed in `Other/`.

Files without an extension and subfolders are left in place. The script moves files, so verify the selected folder before running it.