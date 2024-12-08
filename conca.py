import os

def concatenate_files(directory, output_file):
    """
    Concatenates all non-hidden .py files in a directory into a single output file,
    adding a delimiter with the full relative path of each file. Skips .git and .venv directories.

    Args:
        directory: The directory to search for files.
        output_file: The path to the output file.
    """

    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            if ".git" in root or ".venv" in root:
                continue  # Skip .git and .venv directories

            for filename in files:
                if filename.endswith(".py") and not filename.startswith('.'):
                    filepath = os.path.join(root, filename)
                    relpath = os.path.relpath(filepath, directory)
                    outfile.write(f">>>>>>>>><{relpath}<<<<<<<<<<\n")
                    try:
                        with open(filepath, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                    except UnicodeDecodeError:
                        print(f"Skipping file {filepath} due to encoding error.")
                    outfile.write("\n")

if __name__ == "__main__":
    directory_path = "DocumentStoreManagementSystem/"  # Replace with your actual directory
    output_filename = "concatenated_output.txt"
    concatenate_files(directory_path, output_filename)
