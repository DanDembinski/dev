import requests,time,hue,sys
from datetime import datetime, date

BAD=['TOR','TOW','WRN','SEW','WIN','SVR','SPE']
count=0
hue.connect()

today=date.today()
while count < 450:
	if today!=date.today():
		count=0
		today=date.today()
	print str(datetime.now())
	print "Connecting to Wunderground API"
	r = requests.get("http://api.wunderground.com/api/ec2821eb68a05bd5/alerts/q/OH/44130.json")
	count=count+1
	print "Using api call #%i" % count

	print "Information gathered; Checking alerts now:"
	
	data=r.json()
	
	for type in data['alerts']:
		if type in BAD:
			print "This is bad:"
			print type['description']+'\n'
			hue.alert()
		else:
			print "Who cares:"
			print type['description']+'\n'
	print "No weather warnings"+'\n'
	time.sleep(180)
print "No more api calls"
exit()

