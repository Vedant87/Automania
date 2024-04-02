import argparse
import shutil
from datetime import datetime
import os
import cv2
import numpy as np
import socketio
import eventlet
import eventlet.wsgi
from PIL import Image
from flask import Flask
from io import BytesIO
import json
import pickle
import matplotlib.image as mpimg
import time

from perception import perception_step
from decision import decision_step
from supporting_functions import update_rover, create_output_images

sio = socketio.Server()
app = Flask(__name__)

class RoverState():
    def __init__(self):
        self.img = None
        self.pos = None
        self.yaw = None
        self.vel = None
        self.nav_angles = None
        self.mode = '____'
        self.throttle_set = ____
        self.brake_set = ____
        self.stop_forward = ____
        self.go_forward = ____
        self.max_vel = ____
        self.vision_image = np.zeros((____, ____, ____), dtype=np.float)
        self.worldmap = np.zeros((____, ____, ____), dtype=np.float)
        self.near_sample = ____
        self.picking_up = ____
        self.send_pickup = ____

Rover = RoverState()

@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        global Rover
        Rover, image = update_rover(____, ____)

        if np.isfinite(Rover.vel):
            Rover = perception_step(____)
            Rover = decision_step(____)

            out_image_string1, out_image_string2 = create_output_images(____)

            if Rover.send_pickup and not Rover.picking_up:
                send_pickup()
                Rover.send_pickup = False
            else:
                commands = (Rover.throttle, Rover.brake, Rover.steer)
                send_control(____, out_image_string1, out_image_string2)
        else:
            send_control((0, 0, 0), '', '')

    else:
        sio.emit('manual', data={}, skip_sid=True)

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)
    send_control((0, 0, 0), '', '')

def send_pickup():
    pickup = {}
    sio.emit("pickup", ____, skip_sid=True)
    eventlet.sleep(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Driving')
    parser.add_argument(
        'image_folder',
        type=str,
        nargs='?',
        default='',
        help='Path to image folder. This is where the images from the run will be saved.'
    )
    args = parser.parse_args()
   
    if args.image_folder != '':
        if not os.path.exists(args.image_folder):
            os.makedirs(args.image_folder)
        else:
            shutil.rmtree(args.image_folder)
            os.makedirs(args.image_folder)
   
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
