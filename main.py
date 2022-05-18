
from __future__ import print_function
from myo.utils import TimeInterval
import myo
import sys
import pickle
import json
import socket
import time

msg = ''
HEADERSIZE = 10
ADDRESS = '10.50.115.95'  # socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, 1243))
print(ADDRESS)
s.listen(5)


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
        global msg
        if not self.interval.check_and_reset():
            return

        parts = []
        if self.orientation:
            for comp in self.orientation:
                parts.append('{}{:.3f}'.format(' ' if comp >= 0 else '', comp))
        parts.append(str(self.pose).ljust(10))

        if len(parts) > 4:
            data = {
                # 'x': parts[0],
                # 'y': parts[1],
                # 'z': parts[2],
                # 'w': parts[3],
                'pose': parts[4].split('.')[1].strip()
            }
            msg = pickle.dumps(data)
            print(json.dumps(data))
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

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

# Detección de las coordenadas en los ejes x-y para acotar los movimientos
    def on_orientation(self, event):
        self.orientation = event.orientation
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
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    myo.init("C:\\myo-sdk-win-0.9.0\\bin\\myo64.dll")
    hub = myo.Hub()
    listener = Listener()
    while hub.run(listener.on_event, 500):
        # pass
        time.sleep(.2)
        clientsocket.send(msg)
