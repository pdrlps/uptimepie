#	UptimePie
#		Pedro Lopes
#		hello@pedrolopes.net
#
# Small utility to check website status from UptimeRobot (http://www.uptimerobot.com/).
# Runs custom system command when if monitor is down (i.e., website is down), logs actions to file.
#
# Note: I use this to check if any of my websites is down, and if it is, the script simply restarts the Tomcat server
#
# Use: python up.py <monitors> <mode> <log file> <password>
#		monitors: monitor id list from UptimeRobot service, 0 for all monitors
#		mode: all (logs all checks) or <anything else> (only logs when monitor is down)
#		log file: well... the log file location
#		password: sudo password to run server restart command
#
# Further UptimeRobot monitoring information at http://www.uptimerobot.com/api.asp

import os, sys, json, requests
import simplejson as json
from BeautifulSoup import BeautifulSoup
from datetime import datetime

# UptimeRobot API key configuration
apiKey = '<your api key here>'

# load and parse response from UptimeRobot API
r = requests.get("http://api.uptimerobot.com/getMonitors?apiKey=" + apiKey + "&format=json&monitors=" + sys.argv[1])
c = r.content.replace("jsonUptimeRobotApi(","")[:-1]
j = json.loads(c)

# log and process API response
for item in j['monitors']:
	for monitor in j['monitors'][item]:
		if (monitor['status'] == "8") | (monitor['status'] == "9"):
			with open(sys.argv[3], 'a') as file:
				file.write('\n' + datetime.now().strftime("%Y-%m-%d %H:%M") + ';' + monitor['id'] + ';' + monitor['friendlyname'] + ';' + monitor['url'] + ';' + monitor['status'] + ';restart')
			os.popen("sudo -S service tomcat6 restart", 'w').write(sys.argv[4])
		else:
			if sys.argv[2] == 'all':
				with open(sys.argv[3], 'a') as file:
					file.write('\n' + datetime.now().strftime("%Y-%m-%d %H:%M") + ';' + monitor['id'] + ';' + monitor['friendlyname'] + ';' + monitor['url'] + ';' + monitor['status'] + ';ok')				