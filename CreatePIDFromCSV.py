#import csv     # imports the csv module
import pandas as pd
import sys      # imports the sys module
import urllib2
import uuid
import json
pd.set_option('display.line_width', 5000) 
pd.set_option('display.max_columns', 60) 

# This should do the following 
# 1. download the csv with the data objects
# 2. check if the data object has a PID associated with it
# 2.1 if so, check if the PID's metadata is still correct 
# 2.2 if not, create a PID


# PIDSERVICE_URL="THE_SERVICE_URL_WITH_PREFIX"
PIDSERVICE_URL="https://epic.grnet.gr/api/v2/handles/11239/"
PIDSERVICE_USER="aphrc-demo"
PIDSERVICE_PASSWD=""
#now, create the connection to the API
# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
password_mgr.add_password(None, PIDSERVICE_URL, PIDSERVICE_USER, PIDSERVICE_PASSWD)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)
# use the opener to fetch a URL
opener.open(PIDSERVICE_URL)
# Install the opener.
# Now all calls to urllib2.urlopen use the created opener.
urllib2.install_opener(opener)


DATAURL=''
REPO_URL='http://aphrc.org/catalog/microdata/index.php/catalog/'
# first we open the CSV file with the list of the data sets
# If we have a list of data sets locally, we can open it with the same method
#df = pd.read_csv("search-09-01-14-062754.csv")
df = pd.read_csv("http://aphrc.org/catalog/microdata/index.php/catalog/export/csv?ps=1000")

# Start the loop over data sets
# we need to extract the catalog number and catalogue name for the URL and PID suffix respectively
for row in df.itertuples():
	dataCollectionName=str(row[2])
	dataCollectionNumber=str(row[1])
	SUFFIX =dataCollectionName # this will be updated in the "suffix" section for each dataset
	print "SUFFIX will be ", SUFFIX
	URL=REPO_URL+dataCollectionNumber # this is the URL of the resources 
	print "URL for resource will be ", URL
	URL_TO_OPEN=PIDSERVICE_URL+SUFFIX
	
	#URL_TO_OPEN=PIDSERVICE_URL+"?URL="REPO_URL+dataCollectionNumber
	JSONDATA=[{'type':'URL','parsed_data':URL}]
	JSONDATATOSEND = json.dumps(JSONDATA);
	print JSONDATATOSEND
	print URL_TO_OPEN
	REQUESTDATA = urllib2.Request(URL_TO_OPEN, data=JSONDATATOSEND)
	# REQUESTDATA = urllib2.Request(URL) # use this in the case of POST
	
	#create the headers
	REQUESTDATA.add_header('Content-Type','application/json')
	REQUESTDATA.add_header('Content-Length',len(JSONDATATOSEND))
	
	# creates the PUT or POST method
	REQUESTDATA.get_method = lambda: 'PUT'

	try:
		DATAURL = urllib2.urlopen(REQUESTDATA)
    
	except urllib2.URLError, e:
		print e
		if e.code == 404:
			print "404-Not found"
		if e.code == 401:
			print "401-Authentication failed"    
			#get http code of the request
		if e.code  == 405:
			print "405-Not Allowed"

	if DATAURL:
    # Getting the code
		print "This gets the code: ", DATAURL.code


# show all the PIDs created with APHRC
URL_TO_OPEN=PIDSERVICE_URL+"?URL=*aphrc*"
REQUESTDATA = urllib2.Request(URL_TO_OPEN)

try:
    DATAURL = urllib2.urlopen(REQUESTDATA)
except urllib2.URLError, e:
    if e.code == 404:
        print "404-Not found"
    if e.code == 401:
        print "401-Authentication failed"    

# Deleting 
if DATAURL:
    # Getting the code
    print "This gets the code: ", DATAURL.code
    for pid in DATAURL.readlines():
		print "deleting ", pid
		# check what URL is specified
		REQUESTDATA = urllib2.Request(PIDSERVICE_URL+pid)
		REQUESTDATA.get_method = lambda: 'DELETE' # works :)
		try:
			pidURL = urllib2.urlopen(REQUESTDATA)
		except urllib2.URLError, e:
		
			if e.code == 404:
				print "404-Not found"
			if e.code == 401:
				print "401-Authentication failed"  
			if pidURL:
				print pidURL.read_lines()
