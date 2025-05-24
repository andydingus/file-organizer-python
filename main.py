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
            print(f"Created directory: {subdir_path}")

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip directories and the script itself
        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower() # Ensure consistent matching

        moved = False
        # Check if the file extension matches any category
        for subdir, extensions in subdirectories.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, subdir)
                destination_path = os.path.join(destination_folder, filename)
                try:
                    shutil.move(filepath, destination_path)
                    print(f"Moved: {filename} -> {subdir}/{filename}")
                    moved = True
                    break # Move to the next file once categorized
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
                    moved = True # Avoid trying to move to 'Other' if an error occurred
                    break

        # If the file wasn't moved to a specific category, move it to "Other"
        if not moved:
            other_dir_path = os.path.join(directory, "Other")
            destination_path = os.path.join(other_dir_path, filename)
            try:
                shutil.move(filepath, destination_path)
                print(f"Moved: {filename} -> Other/{filename}")
            except Exception as e:
                print(f"Error moving {filename} to Other: {e}")

    print("File organization complete.")

if __name__ == '__main__':
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # For testing, you might want to create a 'TestFiles' directory
    # in the same location as the script and put some dummy files in it.
    # Example:
    test_dir = os.path.join(script_directory, "TestFilesToOrganize")
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"Created test directory: {test_dir}")
        # You can create some dummy files here for testing
        # open(os.path.join(test_dir, "sample.txt"), 'w').close()
        # open(os.path.join(test_dir, "image.jpg"), 'w').close()
        # open(os.path.join(test_dir, "archive.zip"), 'w').close()
        # open(os.path.join(test_dir, "unknown.xyz"), 'w').close()

    # IMPORTANT: Replace 'your_target_directory' with the actual directory you want to organize.
    # For safety, it's good to test with a sample directory first.
    # target_directory_to_organize = "your_target_directory"
    target_directory_to_organize = test_dir # Using the test directory for this example

    if target_directory_to_organize: # Check if a directory is set
        organize_files(target_directory_to_organize)
    else:
        print("Please set the 'target_directory_to_organize' variable.")