# importing the necesary libraries
import os
import shutil

#asking and scanning the selectionated path
path = input("Enter Path: ")
files = os.listdir(path)

# Checking the extension
for file in files:
	filename,extension = os.path.splitext(file)
	extension = extension[1:]
	
	# Organizing files depending on its extension
	if os.path.exists(path+'/'+extension):
		shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
	# creating new directories depending on its extension
	else:
		os.makedirs(path+'/'+extension)
		shutil.move(path+'/'+file, path+'/'+extension+'/'+file)