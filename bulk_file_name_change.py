import os
k = 1912
def rename_files(folder_path, new_name_prefix):
    # Get a list of all files in the folder
    global k
    files = os.listdir(folder_path)

    # Iterate over each file and rename it
    for i , filename in enumerate(files):
        # Construct the new file name
        new_filename = f"{new_name_prefix}_{k+1}.png"
        k += 1
        
        # Construct the full paths to the old and new files
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

# Example usage:
folder_path = r"C:\Users\srina\Desktop\Pressure data 1"
new_name_prefix = 'frame'
rename_files(folder_path, new_name_prefix)
