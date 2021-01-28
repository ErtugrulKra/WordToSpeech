from flask import Flask
import flask
import os
from flask.helpers import send_file
from flask_restful import Api, Resource
import pyttsx3 as sp

engine = sp.init("espeak")

wordapp=Flask(__name__)
api = Api(wordapp)

class SpeakApi(Resource):
    def get(self,word):
        filePath=word+".mp3"
        if os.path.exists(filePath):
            return send_file(filePath,"application/octet-stream")

        engine.save_to_file(word,word+".mp3")
        engine.runAndWait()
        engine.stop()
        file = open(word+".mp3")
        return send_file(file,"application/octet-stream")
    

api.add_resource(SpeakApi,"/speak/<string:word>")

if __name__ == "__main__":
    wordapp.run(host='0.0.0.0',port=5000)