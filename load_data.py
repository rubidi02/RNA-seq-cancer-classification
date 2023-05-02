import os
import pandas as pd
import pickle
import numpy as np

# Specify the path to the parent directory containing the folders to iterate through
parent_dir = "../data/data-tcga"
sample_sheet_file = "gdc_sample_sheet.2023-04-03.tsv"
clinical_file = "clinical.tsv"
all_data_file_path = "all_data.pkl"
all_labels_file_path = "all_labels.pkl"

def extract_cancer_class(tissue_organ):
    if 'lung' in tissue_organ.lower():
        return 'lung'
    if 'breast' in tissue_organ.lower():
        return 'breast'
    if 'prostate' in tissue_organ.lower():
        return 'prostate'
    return 'unknown'


if not os.path.exists(all_data_file_path):

    # read sample sheet file and clinical file into the memory
    sample_sheet = pd.read_csv(sample_sheet_file, delimiter="\t")
    print(sample_sheet.head(10))

    clinical_sheet = pd.read_csv(clinical_file, delimiter="\t")
    print(clinical_sheet.head(10))

    all_data = []
    all_labels = []

    # Iterate through all folders in the parent directory
    for folder in os.listdir(parent_dir):
        # Create the full path to the folder
        folder_path = os.path.join(parent_dir, folder)
        # Check if the item in the directory is a folder
        if os.path.isdir(folder_path):

            # try to extract the cancer tissue first, if possible
            row = sample_sheet[ sample_sheet['File ID'] == folder ]
            case_id = row['Case ID'].to_numpy()[0]
            case_id = case_id.split(',')[0]
            print(f"Case ID: {case_id}")

            case_id_clinical = clinical_sheet[clinical_sheet['case_submitter_id'] == case_id]
            tissue_organ_origin = case_id_clinical['tissue_or_organ_of_origin'].to_numpy()
            if len(tissue_organ_origin) == 0:
                continue
            else:
                tissue_organ_origin = tissue_organ_origin[0]
                
            tissue_organ_origin = extract_cancer_class(tissue_organ_origin)
            print(f"Organ of origin: {tissue_organ_origin}")

            # tissue extracted successfully!
            all_labels.append(pd.DataFrame([tissue_organ_origin]))


            # extract the gene counts

            # Get a list of all .tsv files in the folder
            tsv_files = [f for f in os.listdir(folder_path) if f.endswith('.tsv')]
            # If there is exactly one .tsv file in the folder, proceed
            if len(tsv_files) == 1:
                # Create the full path to the .tsv file
                tsv_path = os.path.join(folder_path, tsv_files[0])
                # Open the .tsv file and count the number of lines starting with "ENSG"
                
                columns = []
                counts = []
                with open(tsv_path, 'r') as tsv_file:
                    for line in tsv_file:
                        if line.startswith("ENSG"):

                            split_line = line.split('\t')
                            
                            gene_name = split_line[1]
                            tpm = split_line[6]
                            #row_json[gene_name] = tpm
                            columns.append(gene_name)
                            counts.append(tpm)
                #print(counts)

                row_df = pd.DataFrame(counts, dtype=np.float32)
                all_data.append(row_df)

    all_data = pd.concat(all_data, axis=1, ignore_index=True).transpose()
    all_data.columns = columns
    all_labels = pd.concat(all_labels, axis=0, ignore_index=True)

    # store the count matrices and labels into pickle files
    with open(all_data_file_path, 'wb') as all_data_pckl:
        pickle.dump(all_data, all_data_pckl)
    with open(all_labels_file_path, 'wb') as all_labels_pckl:
        pickle.dump(all_labels, all_labels_pckl)

else: # .pkl file exists, load everything from it to skip processing

    with open(all_data_file_path, 'rb') as all_data_pckl:
        all_data = pickle.load(all_data_pckl)
    with open(all_labels_file_path, 'rb') as all_labels_pckl:
        all_labels = pickle.load(all_labels_pckl)


print(all_data)
print(all_labels)


