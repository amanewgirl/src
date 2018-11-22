import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

number=0

#socketio code to handle messages
@socketio.on('my event')
def tryn(int):
   global number
   print(number)
   number=number+1
   emit('my response', number)
   return number
   

#socketio code to handle messages
@socketio.on('message')
def stuff(msg):
    print('Message:' +msg)
    send(msg, broadcast=True)

#this is the base Design across the web app
def design():
    return render_template ('design.html')

#Chat
@app.route("/")
def index():
	return render_template('debateInstructions.html')

#@app.route('/debate')
#def debate():
#	return render_template ('boardFinal.html') 


#debate game
@app.route('/debate')
@app.route('/debate/<player>')
def debate(player=None):
	return render_template ('boardFinalTest.html', player=player)



#error pages	
@app.errorhandler (404)
def page_not_found (error):
	return render_template ('tryagain.html')



if __name__ =="__main__":
     app.run(host='0.0.0.0')
     socketio.run(app, host='0.0.0.0')