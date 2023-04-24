import os
import pandas as pd

# Specify the path to the parent directory containing the folders to iterate through
parent_dir = "data"
sample_sheet_file = "gdc_sample_sheet.2023-04-23.tsv"
clinical_file = "clinical.tsv"

# read sample sheet file into the memory
sample_sheet = pd.read_csv(sample_sheet_file, delimiter="\t")
print(sample_sheet)

# Iterate through all folders in the parent directory
for folder in os.listdir(parent_dir):
    # Create the full path to the folder
    folder_path = os.path.join(parent_dir, folder)
    # Check if the item in the directory is a folder
    if os.path.isdir(folder_path):
        # Get a list of all .tsv files in the folder
        tsv_files = [f for f in os.listdir(folder_path) if f.endswith('.tsv')]
        # If there is exactly one .tsv file in the folder, proceed
        if len(tsv_files) == 1:
            # Create the full path to the .tsv file
            tsv_path = os.path.join(folder_path, tsv_files[0])
            # Open the .tsv file and count the number of lines starting with "ENSG"
            ensg_count = 0
            with open(tsv_path, 'r') as tsv_file:
                for line in tsv_file:
                    if line.startswith("ENSG"):
                        ensg_count += 1

                row = sample_sheet[ sample_sheet['File ID'] == folder ]
                case_id = row['Case ID'].to_numpy()[0]
                print(f"Case ID: {case_id}")

            # Print the count of lines starting with "ENSG" for the current .tsv file
            print(f"Folder {folder} - File {tsv_files[0]}: {ensg_count} lines starting with 'ENSG'")
