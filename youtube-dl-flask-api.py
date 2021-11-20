import flask
from flask import request, Response
from flask import send_file
from flask_cors import CORS
import json
import youtube_dl
import threading
import os
import time

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

CORS(app)

def downloadVideoThread(url):

    ydl = youtube_dl.YoutubeDL()

    info = ydl.extract_info(url, download=True)
    filename = ydl.prepare_filename(info)

    return filename

def backgroundDelete(path):

    time.sleep(300)

    try:
        os.remove(path)
    except:
        pass

@app.route("/download", methods=["GET"])
def home():

    parametersJson = json.loads(json.dumps(request.args))

    try:

        url = parametersJson["url"]
        
        path = downloadVideoThread(url)

        threading.Thread(target=backgroundDelete, args=(path,)).start()

        return send_file(path, as_attachment=True)

    except:
        return "Please enter a valid URL"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)