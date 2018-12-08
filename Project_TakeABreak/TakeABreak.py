import argparse
import sys
import time
import webbrowser 

# Parser for parsing input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--time", help="Flag for specifying interval between pauses, default is 10 seconds", type=float, default=10.0)
parser.add_argument("--isMinute", help="Flag for converting interval between pauses into minutes", type=bool, default=False)
parser.add_argument("--maxNumberOfBreaks", help="Flag for specifying maximum number of breaks, default is 1", type=float, default=1.0)
args = parser.parse_args()

# Parameters for running the job
currentNumberOfBreaks = 0
maxNumberOfBreaks = args.maxNumberOfBreaks
pauseInterval = args.time

# Convert to minutes if necessary
isMinute = args.isMinute
if isMinute:
    pauseInterval = pauseInterval * 60.0

while (currentNumberOfBreaks < maxNumberOfBreaks):
	time.sleep(pauseInterval)
	webbrowser.open ("https://www.youtube.com/watch?v=79DijItQXMM&t=10s")
	currentNumberOfBreaks = currentNumberOfBreaks + 1.0
