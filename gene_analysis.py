#>NM_000207.3 Homo sapiens insulin (INS), transcript variant 1, mRNA
gene = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCC CT TGAACC AGC".replace(" ", "")

length_gene = len(gene)
count_A = gene.count('A')
count_T = gene.count('T')
count_G = gene.count('G')
count_C = gene.count('C')
gc_content= (count_G + count_C) / length_gene * 100
print(len(gene) - (count_A + count_T + count_G + count_C))
print(set(gene) - {"A", "T", "G", "C"})
print('The length of the gene sequence is:', length_gene)
print('The count of each nucleotide in the gene sequence is:', count_A, count_T, count_G, count_C)
print (gc_content)
print(gene[0:10]) 
print (gene[-10:])
print(gene[::-1])
if gene [0:3] == 'ATG':
    print('The gene starts with a start codon')
else:
    print('The gene does not start with a start codon')
    if gene[-1] == 'T' or gene[-1] == 'A' or gene[-1] == 'G' or gene[-1] == 'C':
    
        print("pyrimidine")
    else:
        print("purine")

