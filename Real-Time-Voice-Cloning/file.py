import os
from shutil import copy
import librosa

directory_1 = "/Users/jay/Documents/Real-Time-Voice-Cloning/data/ta_in_male/"

for test in os.listdir(directory_1):
	sr = 16000
	if ".DS_Store" not in test and "LICENSE" not in test and "line_index.tsv" not in test:
		path = directory_1 + test
		print(path)
		y, s = librosa.load(path, sr=16000)
		librosa.output.write_wav(path, y, sr)
my_set = set()


for files in os.listdir(directory_1):
		d = files[4:9]
		my_set.add(d)
print(my_set)


for item in my_set:
	if item !="" :
	  os.mkdir(item)

for file in os.listdir(directory_1):
	d = file[4:9]
	path_1 = directory_1 + file
	if len(d) == 5:
		copy(path_1, d)


    
