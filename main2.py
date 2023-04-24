# Open the file for reading
with open('GSE60052_79tumor.7normal.normalized.log2.data.Rda.tsv', 'r') as f:

    # Initialize the row count to 0
    row_count = 0

    # Loop through each line in the file
    for line in f:

        # Increment the row count
        row_count += 1

    # Print the number of rows
    print("Number of rows:", row_count)
