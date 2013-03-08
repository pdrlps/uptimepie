UptimePie
=========


		Pedro Lopes
		hello@pedrolopes.net


Small utility to check website status from UptimeRobot (http://www.uptimerobot.com/).
Runs custom system command when if monitor is down (i.e., website is down), logs actions to file.

## Note
I use this to check if any of my websites is down, and if it is, the script simply restarts the Tomcat server

## Use
python up.py <monitors> <mode> <log file> <password>
		* monitors: monitor id list from UptimeRobot service, 0 for all monitors
		* mode: all (logs all checks) or <anything else> (only logs when monitor is down)
		* log file: well... the log file location
		* password: sudo password to run server restart command

Further UptimeRobot monitoring information at http://www.uptimerobot.com/api.asp