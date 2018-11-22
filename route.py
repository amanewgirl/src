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


#socketio code to handle messages
#@socketio.on('Card')
#def handleMessage(img):
    #print('Card:' +img)
    #send(img, broadcast=True)



#this is the base Design across the web app
def design():
    return render_template ('design.html')

#Chat
@app.route("/")
def index():
	return render_template('debateInstructions.html')

@app.route('/debate')
def debate():
	return render_template ('indexTest3.html') 

#error pages	
@app.errorhandler (404)
def page_not_found (error):
	return render_template ('tryagain.html')



if __name__ =="__main__":
     app.run(host='0.0.0.0')
     socketio.run(app, host='0.0.0.0')