import glob
import os

for fn in glob.glob('../orient/*fw_R1_orient.fastq.gz'):
	new_fn_1 = fn.split(".")[-3].split("/")[2].split("_R")[0] + "_R1_primertrim.fastq.gz"
	new_fn_2 = fn.split(".")[-3].split("/")[2].split("_R")[0] + "_R2_primertrim.fastq.gz"
	read_1 = fn.split(".")[-3].split("/")[2].split("_R")[0] +"_R1_orient.fastq.gz"
	read_2 = fn.split(".")[-3].split("/")[2].split("_R")[0] +"_R2_orient.fastq.gz"
	out = fn.split(".")[-3].split("/")[2].split("_R")[0]


	print(out)
	print(read_1)

	os.system("cutadapt -g TCACCGTGGGTACAGTAAAAT -G TCCCATCTTCGTTGACT --discard-untrimmed -o " + new_fn_1 + " -p " + new_fn_2 +" ../orient/" + read_1 + " ../orient/" + read_2 + " > " + out + ".out")


for fn in glob.glob('../orient/*rv_R1_orient.fastq.gz'):
	new_fn_1 = fn.split(".")[-3].split("/")[2].split("_R")[0] + "_R1_primertrim.fastq.gz"
	new_fn_2 = fn.split(".")[-3].split("/")[2].split("_R")[0] + "_R2_primertrim.fastq.gz"
	read_1 = fn.split(".")[-3].split("/")[2].split("_R")[0] +"_R1_orient.fastq.gz"
	read_2 = fn.split(".")[-3].split("/")[2].split("_R")[0] +"_R2_orient.fastq.gz"
	out = fn.split(".")[-3].split("/")[2].split("_R")[0]

	print(out)

	os.system("cutadapt -g TCACCGTGGGTACAGTAAAAT -G TCCCATCTTCGTTGACT --discard-untrimmed -o " + new_fn_1 + " -p " + new_fn_2 +" ../orient/" + read_1 + " ../orient/" + read_2 + " > " + out + ".out")

