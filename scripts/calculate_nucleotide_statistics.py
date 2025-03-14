import os

# Directory containing .fa files
directory = r"C:\Users\Cliente\Documents\dissertacao\fasta_mitofish"
# Output .tsv file
output_file = r"C:\Users\Cliente\Documents\dissertacao\estatisticas_mtdna.tsv"

# Function to calculate the percentage of a base in the sequence
def calculate_base_percentage(sequence, base):
    sequence = sequence.upper()
    total = len(sequence.replace('\n', ''))
    count_base = sequence.count(base)
    return (count_base / total) * 100 if total > 0 else 0

# Function to calculate the percentage of AT and GC in the sequence
def calculate_AT_GC_percentage(sequence):
    sequence = sequence.upper()
    total = len(sequence.replace('\n', ''))
    count_AT = sequence.count('A') + sequence.count('T')
    count_GC = sequence.count('G') + sequence.count('C')
    pct_AT = (count_AT / total) * 100 if total > 0 else 0
    pct_GC = (count_GC / total) * 100 if total > 0 else 0
    return pct_AT, pct_GC

# Function to calculate AT skew in the sequence
def calculate_AT_skew(sequence):
    sequence = sequence.upper()
    count_A = sequence.count('A')
    count_T = sequence.count('T')
    total_AT = count_A + count_T
    return (count_A - count_T) / total_AT if total_AT != 0 else 0

# Function to calculate GC skew in the sequence
def calculate_GC_skew(sequence):
    sequence = sequence.upper()
    count_G = sequence.count('G')
    count_C = sequence.count('C')
    total_GC = count_G + count_C
    return (count_G - count_C) / total_GC if total_GC != 0 else 0

# Open the output file for writing
with open(output_file, "w") as out_f:
    # Write the header
    out_f.write("File\tCharacter Count\t% A\t% T\t% G\t% C\t% AT\t% GC\tAT Skew\tGC Skew\n")
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".fa") or filename.endswith(".fasta"):
            # Full file path
            filepath = os.path.join(directory, filename)
            
            # Initialize variables
            char_count = 0
            sequence = ""
            
            # Read the .fa file
            with open(filepath, "r") as f:
                # Skip the first line
                next(f)
                # Read the file content and store the sequence
                for line in f:
                    line = line.strip()
                    char_count += len(line)
                    sequence += line
            
            # Calculate the percentages of A, T, G, C
            pct_A = calculate_base_percentage(sequence, 'A')
            pct_T = calculate_base_percentage(sequence, 'T')
            pct_G = calculate_base_percentage(sequence, 'G')
            pct_C = calculate_base_percentage(sequence, 'C')
            
            # Calculate AT and GC percentages
            pct_AT, pct_GC = calculate_AT_GC_percentage(sequence)
            
            # Calculate AT skew and GC skew
            AT_skew = calculate_AT_skew(sequence)
            GC_skew = calculate_GC_skew(sequence)
            
            # Write the result to the .tsv file
            out_f.write(f"{filename}\t{char_count}\t{pct_A:.2f}\t{pct_T:.2f}\t{pct_G:.2f}\t{pct_C:.2f}\t{pct_AT:.2f}\t{pct_GC:.2f}\t{AT_skew:.2f}\t{GC_skew:.2f}\n")

print(f"Results saved in {output_file}")
