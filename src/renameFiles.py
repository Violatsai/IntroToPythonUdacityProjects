# retrieve file names from a folder
# rename file names
import os
def renameFiles():
	cwd = os.getcwd()
	dst = cwd + "/renamePractice"
	os.chdir(dst)
	
	fileList = os.listdir(dst)
	for fileName in fileList:
		os.rename(fileName, fileName.translate(None,"0123456789"))
	
	fileList = os.listdir(dst)
	for fileName in fileList:
		print("\t" + fileName)

renameFiles()