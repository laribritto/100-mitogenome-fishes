import os
from Bio import SeqIO

# Folder paths
new_folder = r"C:\Users\Cliente\Documents\mitofish-novoplasty"
rRNA_folder = r"C:\Users\Cliente\Documents\dissertacao\rrna"

def extract_rRNA(input_file, output_file):
    with open(output_file, 'w') as out_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            # Check if the record is rRNA and not tRNA
            if '16S' in record.description or '12S' in record.description:
                SeqIO.write(record, out_file, 'fasta')

# Create the output folder if it doesn't exist
if not os.path.exists(rRNA_folder):
    os.makedirs(rRNA_folder)

# Iterate over all files in the new folder and its subfolders
for root, dirs, files in os.walk(new_folder):
    for file in files:
        if file.endswith('.fa'):
            file_path = os.path.join(root, file)
            output_path = os.path.join(rRNA_folder, file)

            extract_rRNA(file_path, output_path)
            print(f"Function extract_rRNA executed for {file_path}. Output saved to {output_path}")
