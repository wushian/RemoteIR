from flask import render_template, redirect
from app import app
from PiController import *
from RemoteDAL import *

@app.route('/')
@app.route('/index')
def index():
		return render_template("index.html", tasks=GetAllTasks())

@app.route('/On')
def immediateActionOn():
	PiOn()
	return redirect("/index",code=302)

@app.route('/Off')
def immediateActionOff():
	PiOff()
	return redirect("/index", code=302)
