import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

#socketio code to handle messages
@socketio.on('message')
def handleMessage(msg):
    print('Message:' +msg)
    send(msg, broadcast=True)


#this is the base Design across the web app
def design():
    return render_template ('design.html')
  
#this is the homepage of the app
@app.route("/", methods = ['POST', 'GET'])
def root():
    return render_template ('home.html')
	
#Chat
@app.route("/in", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
	name = request.form	
    	if request.form ['action'] == 'log in':
		return render_template('index.html')
	

@app.route("/resources")
def help():
    return render_template ('resources.html')
	
@app.route("/look-it-up")
def online_search():
        return render_template ('lookup.html',)
        

#error pages	
@app.errorhandler (404)
def page_not_found (error):
	return render_template ('tryagain.html')

@app.errorhandler (500)
def page_not_found (error):
	return render_template ('home2.html')

if __name__ =="__main__":
     app.run(host='0.0.0.0')
     socketio.run(app, host='0.0.0.0')