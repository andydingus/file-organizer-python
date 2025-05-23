import os
import shutil
import time

def organize_files(directory):
    """Organizes files in the given directory into subdirectories based on file type."""

    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    print(f"Organizing files in: {directory}")

    # Create subdirectories if they don't exist
    subdirectories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Presentations": [".ppt", ".pptx"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
        "Other": [] # For files that don't match any category
    }

    for subdir in subdirectories:
        subdir_path = os.path.join(directory, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip directories and the script itself
        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        moved = False
        # Check if the file extension matches any category
        for subdir, extensions in subdirectories.items():
            if file_extension in extensions:
                destination_path = os.path.join(directory, subdir, filename)
                try:
                    shutil.move(filepath, destination_path)
                    print(