from Bio import SeqIO

# Load the FASTA file
fasta_file = "ecoli.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    print("Name:", record.id)
    print("Length:", len(record.seq), "base pairs")
    print("First 100 bases:", record.seq[:100])
    

    