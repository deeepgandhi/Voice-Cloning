import os 

directory = "SV2TTS_Indian/encoder"
directory_1 = "SV2TTS_Indian/encoder/"

for file in os.listdir(directory):
	if "DS_Store" not in file:
		 count = 0
		 path = directory_1 + file 
		 for files in os.listdir(path):
		 	if "_sources.txt" not in files:
			 	# print(files)
			 	count = count+1
		 if count<5:
		 	print(file)
