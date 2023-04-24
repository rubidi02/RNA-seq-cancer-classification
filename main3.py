import csv

# function to extract the IDs from a TSV file
def extract_ids(filename):
    ids = set()
    with open(filename, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if row[0].startswith('ENSG'):
                ensg_id = row[0].split('.')[0] # ignore everything after the dot
                ids.add(ensg_id)
    return ids

# read the two TSV files and extract the IDs
file1_ids = extract_ids('tcga.tsv')
file2_ids = extract_ids('geo.tsv')

# compare the two sets of IDs
common_ids = file1_ids.intersection(file2_ids)
print(f"{len(common_ids)} IDs appear in both files.")
