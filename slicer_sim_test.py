# This code will call a data_seq and slice it using num_of_slices and
# bp_per_slice. Script will take the inputs and return num_of_slices outputs,
# each with a string length of bp_per_slice.

# The below code might be useful for future stuff.
# from Bio import SeqIO
# from Bio.Seq import Seq
# for seq_record in SeqIO.parse('c_elegans.PRJNA275000.WS267.genomic.fa', 'fasta'):

import numpy as np

print("Welcome to slice sim!")

# Create empty string and bytearray for original sequence.
data_seq = ()
data_seq_ba = bytearray(data_seq, "utf-8")

# Create empty string and an empty list for the original sequence data.
data_seq = ''
list_lines = []

# If the data is too large, the following bytearray could be an option. data_seq_ba = bytearray(data_seq, "utf-8")

# Open file, skip any lines starting with '>', remove end formatting, and append the lines to the list of lines.
with open('test_fa.txt', 'r') as file1:
    for line in file1.readlines():
        if ">" in line:
            continue
        else:
            line=line.strip("\n")
            list_lines.append(line)

# Fill the empty string by joining the list of lines with an empty "" separator.
data_seq="".join(list_lines)

# The below code was my first attempt, which James Johnson helped me fix to the code seen above.
#with open('c_elegans.PRJNA275000.WS267.genomic.fa', 'r') as file1:
#  for i, line in enumerate(file1):
#    if i == 0 or not line.startswith('>'):
#      for line in file1:
#        line.strip('\n')
#        data_seq.join()
#        data_seq_ba.extend()

# Assign variables to user inputs and confirm with a print statement.
print("Please input a numeric value for the following questions.")
num_of_slices = input("How many slices? ")
bp_per_slice = input("How many bp per slice? ")
print("You have chosen to pick  %s slices %s bp in length." % (num_of_slices, bp_per_slice))

# Find length of the sequence
data_length = len(data_seq)

# Import random package, make empty lists, identify a random number of slice starting positions within the length of the original sequence, identify the starting positions' related end positions for the given slice length.
import random
slice_pos_start = []
for x in range(num_of_slices):
	slice_pos_start.append(random.randint(1, data_length - bp_per_slice))
slice_pos_end = []
for x in range(slice_pos_start):
  slice_pos_end.append(slice_pos_start + bp_per_slice + 1)

# Create empty dictionary. Keys are the slice_position list.  Values are the slice from data_seq.
slice_dict = {}
for x in range(slice_pos_start):
	slice_dict[x] = data_seq[slice_pos_start:slice_pos_end]

# Create an empty string for the mutated sequence
data_seq_mut = ''

# Define a new function called mutate. This code only looks at transitions, not transversions.  Maybe I can use this in the future. prob_* is the probability of the listed transition given as a float where 1.0 is 100%.
def mutate(sequence, prob_AtoG, prob_GtoA, prob_CtoT, prob_TtoC):
  for i, char in enumerate(sequence):
    if char == "A":
      if random.uniform(0.0, 1.0) < prob_AtoG:
        sequence[i] = "G"
    elif char == "C":
      if random.uniform(0.0, 1.0) < prob_CtoT:
        sequence[i] = "T"
    elif char == "G":
      if random.uniform(0.0, 1.0) < prob_GtoA:
        sequence[i] = "A"
    elif char == "T":
      if random.uniform(0.0, 1.0) < prob_TtoC:
        sequence[i] = "C"
    else:
      continue

# Make random mutations at random positions of data_seq and fill data_seq_mut
data_seq_mut = mutate(data_seq, 0.0001, 0.0001, 0.0001, 0.0001)

# Import random package, make empty lists, identify a random number of slice starting positions within the length of the original sequence, identify the starting positions' related end positions for the given slice length.
import random
mut_slice_pos_start = []
for x in range(num_of_slices):
	mut_slice_pos_start.append(random.randint(1, data_length - bp_per_slice))
mut_slice_pos_end = []
for x in range(mut_slice_pos_start):
  mut_slice_pos_end.append(mut_slice_pos_start + bp_per_slice + 1)

# Create empty dictionary. Keys are the slice_position list.  Values are the slice from data_seq.
mut_slice_dict = {}
for x in range(mut_slice_pos_start):
	mut_slice_dict[x] = data_seq_mut[mut_slice_pos_start:mut_slice_pos_end]

# Output files
with open("mutated_sequence.txt", 'w') as output_file1:
    output_file1.write(data_seq_mut)
with open("slices_original.txt", 'w') as output_file2:
    output_file2.write(slice_dict)
with open("slices_mutated.txt", 'w') as output_file3:
    output_file3.write(mut_slice_dict)