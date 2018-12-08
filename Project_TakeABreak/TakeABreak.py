# This is Viola's first python program!
# This program urges users to take a break
# every two hours 
import time
import webbrowser 
currentTime = 0
while (currentTime<=2):
	time.sleep (5)
	webbrowser.open ("https://www.youtube.com/watch?v=79DijItQXMM")
	currentTime = currentTime + 1