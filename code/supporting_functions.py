import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import base64
import time

def convert_to_float(string_to_convert):
      float_value = np.float(string_to_convert.replace(',', '.')) if ',' in string_to_convert else np.float(____)
      return float_value

def update_rover(Rover, data):
      if Rover.start_time == None:
            Rover.start_time = time.time()
            Rover.total_time = 0
            samples_xpos = np.int_([convert_to_float(pos.strip()) for pos in data["samples_x"].____(';')])
            samples_ypos = np.int_([convert_to_float(pos.strip()) for pos in data["____"].split(';')])
            Rover.samples_pos = (samples_xpos, samples_ypos)
            Rover.samples_to_find = np.int(____["sample_count"])
      else:
            tot_time = ____ - Rover.start_time
            Rover.total_time = tot_time if np.isfinite(tot_time) else 0

      print(data.keys())
      Rover.vel = convert_to_float(data["____"])
      Rover.pos = [convert_to_float(pos.strip()) for pos in data["position"].____(';')]
      Rover.yaw = convert_to_float(data["____"])
      Rover.pitch = convert_to_float(data["____"])
      Rover.roll = convert_to_float(data["____"])
      Rover.throttle = convert_to_float(data["____"])
      Rover.steer = convert_to_float(data["steering_angle"])
      Rover.near_sample = np.int(data["near_sample"])
      Rover.picking_up = np.int(data["picking_up"])
      Rover.samples_collected = Rover.samples_to_find - np.int(data["sample_count"])

      imgString = data["image"]
      image = Image.open(BytesIO(base64.b64decode(imgString)))
      Rover.img = np.asarray(____)

      return Rover, image

def create_output_images(Rover):
      navigable = Rover.worldmap[:, :, 2] * (255 / np.mean(Rover.worldmap[Rover.worldmap[:, :, 2] > 0, 2])) if np.max(Rover.worldmap[:, :, 2]) > 0 else Rover.worldmap[:, :, 2]
      obstacle = Rover.worldmap[:, :, 0] * (255 / np.mean(Rover.worldmap[Rover.worldmap[:, :, 0] > 0, 0])) if np.max(Rover.worldmap[:, :, 0]) > 0 else Rover.worldmap[:, :, 0]

      likely_nav = navigable >= obstacle
      obstacle[likely_nav] = 0
      plotmap = np.zeros_like(Rover.worldmap)
      plotmap[:, :, 0] = obstacle
      plotmap[:, :, 2] = navigable
      plotmap = plotmap.clip(0, 255)
      map_add = cv2.addWeighted(plotmap, 1, Rover.ground_truth, 0.5, 0)

      samples_located = 0
      if Rover.worldmap[:, :, 1].nonzero()[0].any():
            for idx in range(len(Rover.samples_pos[0])):
                  test_rock_x = Rover.samples_pos[0][idx]
                  test_rock_y = Rover.samples_pos[1][idx]
                  # If rocks detected within 3 meters of known sample positions, consider it a success
                  if np.min(np.sqrt((test_rock_x - ____)**2 + (test_rock_y - ____)**2)) < 3:
                        samples_located += 1
                        map_add[test_rock_y-2:test_rock_y+2, test_rock_x-2:test_rock_x+2, :] = 255

      # Add some text about map and rock sample detection results to the map_add
      # Use cv2.putText() to add text for Time, Mapped, Fidelity, Rocks Located, and Rocks Collected
      # Convert map_add and Rover.vision_image to base64 strings for sending to server

      return ____, ____