#importing packages 
from Bio import SeqIO
import os


fasta_sequences = []

for file in os.listdir('input_data'):

    sequence = SeqIO.read('input_data/'+file, 'fasta')

    #change id to just scientific name
    name = os.path.splitext(file)[0]
    sequence.id = name

    fasta_sequences.append(sequence)

#combines all the sequences into 1 file
caninae = SeqIO.write(fasta_sequences, 'output_data/caninae.fasta', 'fasta')


