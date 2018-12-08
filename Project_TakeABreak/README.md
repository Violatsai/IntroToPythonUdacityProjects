# Project: Take-A-Break

Project Take-A-Break utilizes while loop to create a project to play my favorite youtube music video ("You're Welcome" from Moana) once every while to remind you to take a break!

To run it, make sure you have __python2__  installed, and simply run the following command in your terminal:
<pre>
> python TakeABreak.py 
</pre>
, the terminal will prompt a youtube page after 10 seconds, enjoy the music!

This is also a large scale project, from which I first learn to parse the input arguments! You can specify the interval between pauses, whether the interval is in minutes or seconds, and the number of pauses! Here are some demo commands
<pre>
> python TakeABreak.py --time 5
</pre>
will prompt the YouTube video just __2__ seconds after the command.
<pre>
> python TakeABreak.py --time 7 --isMinute True
</pre>
will convert the interval into minutes, and hence prompt the YouTube videos 7 minutes after the command. Finally, 
<pre>
> python TakeABreak.py --maxNumberOfBreaks 5
</pre>
will rerun the prompts for 5 times. All input arguments can be mixed up, so feel free to try commands like
<pre>
> python TakeABreak.py --time 20 --isMinute True --maxNumberOfBreaks 3
</pre>
, which will prompt up the YouTube video every 20 minutes within the upcoming hour.
