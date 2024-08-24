import os

def rename_files(directory):
    # List of alphabetical prefixes
    prefixes = [chr(i) for i in range(ord('A'), ord('L') + 1)]
    # Number of files for each prefix
    num_files_per_prefix = 18
    
    # List .jpg and .RAW files
    jpg_files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.jpg')])
    raw_files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.raw')])

    # Check if there are exactly 216 .jpg and 216 .raw files
    if len(raw_files) != 216:
        print("There should be exactly 216 .jpg files and 216 .raw files in the directory.")
        return

    # Renaming .jpg files
    count = 1
    for prefix in prefixes:
        for i in range(1, num_files_per_prefix + 1):
            old_name = jpg_files[count - 1]
            new_name = f"{prefix}{i}.JPG"
            os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            count += 1
    
    # Renaming .raw files
    count = 1
    for prefix in prefixes:
        for i in range(1, num_files_per_prefix + 1):
            old_name = raw_files[count - 1]
            new_name = f"{prefix}{i}.RAW"
            os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            count += 1

    print("Renaming completed.")

# Replace 'your_directory_path' with the path to your directory containing the files
rename_files("E:\\Dataset Multispectral\\Dataset_Mapir\\NormalRGN_Unpad\\2024_0608")