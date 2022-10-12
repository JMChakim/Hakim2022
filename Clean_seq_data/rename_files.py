import glob
import os


f = open('../../Metadata/Sample_to_MID_sequencingname.csv')

filename_meta = {}
MID_meta = {}

for line in f.readlines():
	filename_meta[line.split(",")[5].strip()] = line.split(",")[0].strip()
	MID_meta[line.split(",")[-1].strip()] = line.split(",")[2].strip()
f.close()
print(filename_meta)
#print(MID_meta)

for fn in glob.glob('./concat/*.gz'):
	filename = (fn.split("/")[-1].split(".fastq")[0].strip())
	readdirection = fn.split("R")[-1].split("_trim")[0]
	MID = fn.split("/")[-1].split(".fastq")[0].split("trim_")[-1].strip()
	
	print(filename)

	if filename in filename_meta:
		os.system("cp " + fn + " ./renamed/" + filename_meta[filename] +"_"+ MID_meta[filename] + "_R" + readdirection + ".fastq.gz")
		#os.system("cp " + fn + " ./" + filename_meta[filename] +"_"+ MID_meta[MID] + "_R" +readdirection + ".fastq.gz")
		print("match")