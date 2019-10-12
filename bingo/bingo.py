from flask import Flask, render_template, session, escape, request, Response
from flask import url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify
import os, sys
import socketio
import socket, eventlet

sio = socketio.Server()
app = Flask(__name__)
app.secret_key = "antyakshari"
app.url_map.strict_slashes = False

@app.route('/')
def peoplebingo(**kwargs):
    return make_response(open('peoplebingo.html').read())

global bingocounter
bingocounter = 0
@sio.on('bingoconnect')
def bingoconnect(sid, environ):
    global bingocounter
    bingocounter += 1
    demo = socket.gethostbyname(socket.gethostname())
    print('bingo connect ' + str(bingocounter), sid)

@sio.on('bingofinish')
def bingofinish(sid, data):
    checkpoint = ['row1', 'row2', 'row3', 'row4', 'row5', 'col1', 'col2', 'col3', 'col4', 'col5', 'rightcross', 'leftcross']
    print(data.split("#")[0] + " has finished " + checkpoint[int(data.split("#")[1])])


if __name__ == "__main__":
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

