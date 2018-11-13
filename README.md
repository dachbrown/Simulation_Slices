# Simulation_Slices
Simulate sequencing with slices

The test file is used with an excerpt of the genome of C elegans to enable faster testing.

The main file is used in combination with a fasta file that contains mostly the entire genome of C elegans.

The purpose of these files is to simulate the action of a sequencer.  The file takes an input fasta or text file and slices it in random positions to simulate sequencing.  It also then mutates the original sequence and slices that mutant in random places.  The point is to compare how the two are assembled to have an idea of the comparison between actual and observed mutation rate.
