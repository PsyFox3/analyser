import os
from flask import Flask, flash, request, redirect, url_for, abort, send_file, render_template
from werkzeug.utils import secure_filename
from flask_restful import Resource, reqparse

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = ['txt', 'log']
CLIENTS = {'client1': 'conf1.cfg', 
           'client2': 'blacklist.cfg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(self, filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class upload(Resource):
    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return {'message': request.url}, 302
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {'message': 'uploaded_file'}, 302

class get_config(Resource):
    def get_config(self, client):
        if client not in CLIENTS:
            return 404
        else:
            filename = 'config\\' + CLIENTS[client]
            return send_file(filename, mimetype='text/plain')
