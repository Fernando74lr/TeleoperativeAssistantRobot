"""
This example displays the orientation, pose and RSSI as well as EMG data
if it is enabled and whether the device is locked or unlocked in the
terminal.

Enable EMG streaming with double tap and disable it with finger spread.
"""

from __future__ import print_function
from myo.utils import TimeInterval
import myo
import sys
import json
from socket.server import server

current_data = ''

class Listener(myo.DeviceListener):

  def __init__(self):
    self.interval = TimeInterval(None, 0.05)
    self.orientation = None
    self.pose = myo.Pose.rest
    self.emg_enabled = False
    self.locked = False
    self.rssi = None
    self.emg = None

  def output(self):
    if not self.interval.check_and_reset():
      return

    parts = []
    if self.orientation:
      for comp in self.orientation:
        parts.append('{}{:.3f}'.format(' ' if comp >= 0 else '', comp))
    parts.append(str(self.pose).ljust(10))
    # parts.append('E' if self.emg_enabled else ' ')
    # parts.append('L' if self.locked else ' ')
    # parts.append(self.rssi or 'NORSSI')
    # if self.emg:
    #   for comp in self.emg:
    #     parts.append(str(comp).ljust(5))
    # print('\r' + ''.join('[{}]'.format(p) for p in parts), end='')
    # print('POSE: ' + parts[0])
    # print(parts)
    if len(parts) > 4:
      print(json.dumps({
        'x': parts[0],
        'y': parts[1],
        'z': parts[2],
        'w': parts[3],
        'pose': parts[4]
      }))
      current_data = str(json.dumps({
        'x': parts[0],
        'y': parts[1],
        'z': parts[2],
        'w': parts[3],
        'pose': parts[4]
      }))
    # print('X: ' + parts[1])
    # print('Y: ' + parts[2])
    # print('Z: ' + parts[3])
    # print('W: ' + parts[4])
    sys.stdout.flush()

  def on_connected(self, event):
    event.device.request_rssi()

  def on_rssi(self, event):
    self.rssi = event.rssi
    self.output()

  def on_pose(self, event):
    self.pose = event.pose
    if self.pose == myo.Pose.double_tap:
      event.device.stream_emg(True)
      self.emg_enabled = True
    elif self.pose == myo.Pose.fingers_spread:
      event.device.stream_emg(False)
      self.emg_enabled = False
      self.emg = None
    self.output()

#Detección de las coordenadas en los ejes x-y para acotar los movimientos
  def on_orientation(self, event):
    self.orientation = event.orientation
    

    # #Up+ and down-
    # if self.orientation.x > 0.4 and self.orientation.x < 0.6:
    #     print("Up")
    # elif self.orientation.x < -0.4 and self.orientation.x > -0.4:
    #   print("Down")

    # #Left- and right+
    # if self.orientation.y > 0.2 and self.orientation.y < 0.7:
    #     print("Right")
    # elif self.orientation.y < -0.3 and self.orientation.y > -0.5:
    #     print("Left")

    ##########Invertido###########    

    #Up- and down+
    if self.orientation.x > 0.2 and self.orientation.x < 0.6:
        print("Down")
    elif self.orientation.x < -0.1 and self.orientation.x > -0.6:
      print("Up")

    #Left+ and right-
    if self.orientation.y > 0.3 and self.orientation.y < 0.7:
        print("Left")
    elif self.orientation.y < -0.3 and self.orientation.y > -0.5:
        print("Right")

    self.output()

  def on_emg(self, event):
    self.emg = event.emg
    self.output()

  def on_unlocked(self, event):
    self.locked = False
    self.output()

  def on_locked(self, event):
    self.locked = True
    self.output()


if __name__ == '__main__':
  myo.init("C:\\myo-sdk-win-0.9.0\\bin\\myo64.dll")
  hub = myo.Hub()
  listener = Listener()
  while hub.run(listener.on_event, 500):
    server(current_data)