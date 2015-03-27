import sys, time
from beautifulhue.api import Bridge
username = 'beautifulhue'
bridge = Bridge(device={'ip':'192.168.1.106'}, user={'name':username})

def createConfig():
	created = False
	print 'Press the button'
	while not created:
		resource = {'user':{'devicetype': 'beautifulhue', 'name': username}}
		response = bridge.config.create(resource)['resource']
		if 'error' in response[0]:
			print 'Unhandled error creating config'
			sys.exit(response)
		else:
			created = True

def getSystemData():
	resource = {'which':'system'}
	return bridge.config.get(resource)['resource']

def alert():
	red={'which':2,'data':{'state':{'xy':[0.675,0.322],'sat':255,'hue':65280}}}
	bridge.light.update(red)
	time.sleep(1.5)
	print red
	resource={
 	       'which':2,
		'data':{
			'state':{"alert":"select"}
       			 }
		}
	x=0
	while x<5:
		x=x+1
		bridge.light.update(resource)
		time.sleep(1)	
		bridge.light.update(resource)
	return()

def connect():
	response = getSystemData()

	if 'lights' in response:
		print 'Connected to the Hub'+'\n'
		return
	elif 'error' in response[0]:
		error = response[0]['error']
		if error['type'] == 1:
			createConfig()
			main()
def allLoop():
	resource={'which':0,'data':{'action':{'on':True,'xy':[0.675,0.322],'sat':255,'bri':255,'effect':'colorloop'}}}
	bridge.group.update(resource)
	return
def allOff():
	resource={'which':0,'data':{'action':{'on':False}}}
	bridge.group.update(resource)
	return
def main():
	connect()
	while True:
		print '1.) alert'
		print '2.) All Loop'
		print '3.) All Off'
		choice=input('Make your choice:')
		if choice == 1:
			alert()
		elif choice == 2:
			allLoop()
		elif choice == 3:
			allOff()
		else:
			print 'No'
			exit()
main()

