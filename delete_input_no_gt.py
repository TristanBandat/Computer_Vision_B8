import os

def find_matching_pairs(folder1, folder2):
    # Get the list of files in each folder
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # Find matching pairs based on the naming pattern
    matching_pairs = files1.intersection(files2)
    return matching_pairs


def delete_non_matching_files(folder1, folder2):
    for filename in os.listdir(folder1):
        parts = filename.split("_")
        file_key = f"{parts[0]}_{parts[1]}_integral.png"
        folder2_files = os.listdir(folder2)
        # Delete files that do not have a matching pair in the other folder
        if file_key not in folder2_files:
            file_path = os.path.join(folder1, filename)
            os.remove(file_path)
            print(f"Deleted: {filename}")


# Replace these paths with the actual paths to your folders
folder_path1 = r"cnn_test_input/x"
folder_path2 = r"cnn_test_input/y"

delete_non_matching_files(folder_path1, folder_path2)