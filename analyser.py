from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta_file = "ecoli.fasta"
motif = "ATG"

print("=" * 50)
print("   DNA SEQUENCE ANALYSER")
print("=" * 50)

with open("results.txt", "w") as out:
    for record in SeqIO.parse(fasta_file, "fasta"):
        gc = gc_fraction(record.seq) * 100
        count = record.seq.count(motif)
        length = len(record.seq)

        lines = [
            f"Genome: {record.id}",
            f"Length: {length} base pairs",
            f"GC Content: {gc:.2f}%",
            f"ATG motif count: {count}",
        ]

        for line in lines:
            print(line)
            out.write(line + "\n")

print("=" * 50)
print("Results saved to results.txt")