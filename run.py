#!flask/bin/python
from app import app
from Scheduler import Scheduler
import threading


t = threading.Thread(target=Scheduler.start)
t.start()
print "Started polling"
app.run(debug = True, host="0.0.0.0")
print "Started server"

@app.teardown_appcontext
def shutdown_session(exception=None):
	app.db_session.remove()