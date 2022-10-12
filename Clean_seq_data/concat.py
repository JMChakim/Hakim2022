import glob
import os


for fn in glob.glob('./unconcat/*_R.fastq.gz'):
	f_name = fn.replace("_R.fastq.gz",".fastq.gz")
	name = f_name.split("/")[-1].replace(".fastq.gz",".fastq.gz")
	print([fn, f_name])
	os.system("cat " + fn + " " + f_name + " > concat/" + name)

