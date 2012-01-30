import os
import pymongo
from flask import Flask, request, make_response, Response, redirect
from mako.template import Template
import simplejson as json


app = Flask(__name__)
app.config.from_object(__name__)

if os.environ.get('BROKER_URL'):
	app.config.from_object('conf.Config')
else:
	app.config.from_envvar('WORKER1_CONFIG')

APP_ID = os.environ.get('FACEBOOK_APP_ID')
APP_SECRET = os.environ.get('FACEBOOK_SECRET')

def connect_to_database():
	DBPATH=os.environ.get('MONGODBPATH')
	DBNAME=os.environ.get('MONGODBDATABASE')
	connection = pymongo.Connection(DBPATH)
	db = connection[DBNAME]
	return db

def get_checkins(username, database, token):
	checkinOffset = 0
	offsetInterval=300
	checkinsTemp = []
	checkins = []

	query1 = "\"query1\":\"SELECT uid2 FROM friend WHERE uid1=me() LIMIT %s" % offsetInterval
	query2 = "\"query2\":\"SELECT page_id, author_uid FROM checkin WHERE author_uid IN (SELECT uid2 FROM #query1)\""
	query3 = "\"query3\":\"SELECT name FROM place WHERE page_id IN (SELECT page_id FROM #query2)\""

	if not database.find_one({'username':username}):
		while checkinsTemp or checkinOffset == 0:	
			checkinsTemp = fql("{%s OFFSET %s\",%s}" % (query1, checkinOffset, query2), token)['data'][1]['fql_result_set']
			checkins+=sort_checkins(checkinsTemp)
			checkinOffset+=offsetInterval


		database.insert({'username':username, 'checkins':checkins})
	else:
		pass

	return database.find_one({'username':username})['checkins']
		
@app.route('/', methods=['GET', 'POST'])
def callback():
	if request.method == 'GET':
		#username = request.args.get('user')
		#database = connect_to_database()
		#collection = database.test
		#collection.insert({'username':username})
		Template(filename='index.html').render()
		print 10
		x = make_response(5)
		return x
	else:
		return redirect('http://www.google.com')
		
		
		
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)