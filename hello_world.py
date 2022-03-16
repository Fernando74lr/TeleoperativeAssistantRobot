"""
This simple example demonstrates how to implement a Device Listener and
how to stop the event flow when the double tap pose is recognized.
"""

from __future__ import print_function
import myo


class Listener(myo.DeviceListener):

  def on_connected(self, event):
    print("Hello, '{}'! Double tap to exit.".format(event.device_name))
    event.device.vibrate(myo.VibrationType.short)
    event.device.request_battery_level()

  def on_battery_level(self, event):
    print("Your battery level is:", event.battery_level)

  def on_pose(self, event):
    if event.pose == myo.Pose.double_tap:
      return False


if __name__ == '__main__':
  myo.init("C:\\myo-sdk-win-0.9.0\\bin\\myo64.dll")
  hub = myo.Hub()
  listener = Listener()
  while hub.run(listener.on_event, 500):
    pass
  print('Bye, bye!')