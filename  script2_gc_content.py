from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta_file = "ecoli.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    gc = gc_fraction(record.seq) * 100
    print(f"Name: {record.id}")
    print(f"GC Content: {gc:.2f}%")
    print("(E. coli should be around 50.8% - let's see if yours matches!)")
    