import os

def combine_ne_files(source_folder, output_file):
    """
    Combine the contents of all .ne files from a folder into a single .txt file.

    Args:
        source_folder (str): Path to the folder containing .ne files.
        output_file (str): Path to the output .txt file.
    """
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through all files in the source folder
        for file_name in os.listdir(source_folder):
            # Check if the file has a .ne extension
            if file_name.endswith('.ne'):
                file_path = os.path.join(source_folder, file_name)

                # Open the .ne file and read its contents
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content + '\n')  # Write the content to the output file
                    print(f"Added content from: {file_name}")

    print(f"All .ne files have been combined into: {output_file}")

# Example Usage
source_folder = "/Users/pigeonyue/Downloads/BBN-NE/training_files"  # Replace with the folder containing .ne files
output_file = "/Users/pigeonyue/Downloads/BBN-NE/training_data_combined.txt"  # Replace with the desired output file path

combine_ne_files(source_folder, output_file)
