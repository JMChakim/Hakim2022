## DOES NOT REVERSE COMPLIMENT
import glob
import os
from Bio import SeqIO

print("opening blast file...")

f = open('blast_R1.out')

print("reading blast file...")

read_to_direction = {}
for line in f.readlines():
	read_name = line.split("\t")[0]
	read_direction = line.split("\t")[5]
	align_length = int(line.split("\t")[4])
	if align_length > 200 and read_name not in read_to_direction:
		read_to_direction[read_name] = read_direction
f.close()

print( "unzipping ")
#unzip the files
for fn in glob.glob('../renamed/*_R1.fastq.gz'):
	unzipped_fn_1 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R1_unzipped.fastq"
	os.system("zcat" + " " + fn + " > ./" + unzipped_fn_1)

for fn in glob.glob('../renamed/*R2.fastq.gz'):
	unzipped_fn_2 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R2_unzipped.fastq"
	os.system("zcat" + " " + fn + " > ./" + unzipped_fn_2)


include1 = {}
include2 = {}

#for read 1
for fn in glob.glob('../renamed/*R1.fastq.gz'):
	unzipped_fn_1 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R1_unzipped.fastq"
	unzipped_fn_2 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R2_unzipped.fastq"

	print("Working on file " + unzipped_fn_1)

	record_list = set()	 	
		
	for record in SeqIO.parse(unzipped_fn_1, 'fastq'):

		if record.id in read_to_direction and record.id not in record_list:

			read_direction = read_to_direction[record.id]

			if read_direction == 'plus':
				include1[record.id] = record
			elif read_direction == 'minus':
				# record.letter_annotations["phred_quality"].reverse()
				# record.seq = record.seq.reverse_complement()
				include2[record.id] = record
					
		record_list.add(record.id)

# For read 2
for fn in glob.glob('../renamed/*R2.fastq.gz'):
	new_fn_name_R1_fw = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "fw_R1_orient.fastq"
	new_fn_name_R2_fw = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "fw_R2_orient.fastq"
	new_fn_name_R1_rv = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "rv_R1_orient.fastq"
	new_fn_name_R2_rv = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "rv_R2_orient.fastq"
	unzipped_fn_1 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R1_unzipped.fastq"
	unzipped_fn_2 = fn.split(".")[-3].split("/")[2].split("_R")[0]  + "_R2_unzipped.fastq"

	print("Working on file " + new_fn_name_R2_fw)

	record_list = set()

	with open(new_fn_name_R1_fw, 'w+') as handleR1fw, open(new_fn_name_R2_fw, 'w+') as handleR2fw, open(new_fn_name_R1_rv, 'w+') as handleR1rv, open(new_fn_name_R2_rv, 'w+') as handleR2rv:
		
		for record in SeqIO.parse(unzipped_fn_2, 'fastq'):

			if record.id in read_to_direction and record.id not in record_list:

				read_direction = read_to_direction[record.id]

				if read_direction == 'plus' and record.id in include1:
					SeqIO.write(record, handleR2fw, 'fastq')
					SeqIO.write(include1[record.id], handleR1fw, 'fastq')

				elif read_direction == 'minus' and record.id in include2:
					# record.letter_annotations["phred_quality"].reverse()
					# record.seq = record.seq.reverse_complement()
					SeqIO.write(record, handleR1rv, 'fastq')
					SeqIO.write(include2[record.id], handleR2rv, 'fastq')
					
			record_list.add(record.id)