from flask import Flask, request
from flask_restful import Resource, Api
from multiprocessing import Process
import time

class Sekolah(Resource):
    def get(self):
        action_process = Process(target=Sekolah.testing(self))
        action_process.start()
        action_process.join(timeout=10)
        action_process.terminate()
        return {
            "test": 123
        }

    def post(self):
        action_process = Process(target=Sekolah.testing(self))
        action_process.start()
        action_process.join(timeout=10)
        action_process.terminate()
        print(request.get_json())
        return request.get_json()

    def testing(self):
        i = 0
        while i != 10:
            i += 1
            time.sleep(1)