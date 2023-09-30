import os
import shutil
import difflib

# Define the file path you want to track
file_path = r'C:/Users/Dell/Desktop/storage/timeline/2023/september/version_control/auto_track.py'

# Define the directory to store version history
version_history_dir = r'C:\Users\Dell\Desktop\local_version'

# Function to create a backup of the file
def backup_file(file_path, version_history_dir):
    if not os.path.exists(version_history_dir):
        os.makedirs(version_history_dir)
    backup_path = os.path.join(version_history_dir, f'version_{len(os.listdir(version_history_dir)) + 1}_{os.path.basename(file_path)}')

    # Close the file before copying
    with open(file_path, 'rb') as src_file, open(backup_path, 'wb') as dest_file:
        shutil.copyfileobj(src_file, dest_file)
    
    print(f'Backup created: {backup_path}')

# Function to compare two files and display differences
def show_file_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.unified_diff(f1.readlines(), f2.readlines(), lineterm='')
        print('\n'.join(diff))

# Create an initial backup
backup_file(file_path, version_history_dir)

while True:
    input("Press Enter to check for changes...")
    
    # Check if the file has been modified
    if os.path.exists(file_path):
        h=r'C:\Users\Dell\Desktop\local_version'
        show_file_diff(file_path, file2=h)
        backup_file(file_path, version_history_dir)
    else:
        print(f"The file '{file_path}' no longer exists.")