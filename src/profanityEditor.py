import urllib

#read text
def readText():
	quotes = open("/Users/viola2114/Desktop/PythonPractice/movie_quotes.txt")
	contentsOfFile = quotes.read()
	print(contentsOfFile)
	quotes.close()
	checkProfanity(contentsOfFile)
	
#detect curse words

def checkProfanity(textToCheck):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + textToCheck)
	output = connection.read()
	#print(output)

	if "true" in output:
		print("profanity alert")
	elif "false" in output:
		print("There is no curse words in this document.")
	else:
		print("Could not scan this document properly.")
	connection.close()

readText()
