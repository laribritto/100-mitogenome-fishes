import os
from Bio import SeqIO

# Folder paths
new_folder = r"C:\Users\Cliente\Documents\mitofish-novoplasty"
tRNA_folder = r"C:\Users\Cliente\Documents\tRNA"

def extract_tRNA(input_file, output_file):
    """Extracts tRNA records from a FASTA file and saves them to a new file."""
    with open(output_file, 'w') as out_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            if 'tRNA' in record.description:
                SeqIO.write(record, out_file, 'fasta')

# Create the destination folder if it doesn't exist
if not os.path.exists(tRNA_folder):
    os.makedirs(tRNA_folder)

# Iterate over all files in the new folder and its subfolders
for root, dirs, files in os.walk(new_folder):
    for file in files:
        if file.endswith('genes.fa'):
            file_path = os.path.join(root, file)
            output_path = os.path.join(tRNA_folder, file)

            # Execute the function to extract tRNA
            extract_tRNA(file_path, output_path)
            print(f"Function extract_tRNA executed for {file_path}. Output saved to {output_path}")
