import socket
import pickle
from interbotix_xs_modules.locobot import InterbotixLocobotXS

HEADERSIZE = 10
ADDRESS = '10.50.115.95'  # socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 1243))

# This script makes the end-effector perform pick, pour, and place tasks
#
# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx250s show_lidar:=true'
# Then change to this directory and type 'python bartender.py'

locobot = InterbotixLocobotXS(
    robot_model="locobot_wx250s", arm_model="mobile_wx250s")


def gripperClose():
    locobot.gripper.close(2.0)


def gripperOpen():
    locobot.gripper.open(2.0)


def moveLeft():
    val = float(input('Y: '))
    locobot.arm.set_ee_cartesian_trajectory(y=val)


def moveRight():
    val = float(input('Y: ')) * -1
    locobot.arm.set_ee_cartesian_trajectory(y=val)


def moveFront():
    val = float(input('X: '))
    locobot.arm.set_ee_cartesian_trajectory(x=val)


def moveBack():
    val = float(input('X: ')) * -1
    locobot.arm.set_ee_cartesian_trajectory(x=val)


def moveUp():
    val = float(input('Z: '))
    locobot.arm.set_ee_cartesian_trajectory(z=val)


def moveDown():
    val = float(input('Z: ')) * -1
    locobot.arm.set_ee_cartesian_trajectory(z=val)


def home():
    locobot.arm.go_to_home_pose()


def sleep():
    locobot.arm.go_to_sleep_pose()


def main():
    home()
    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = s.recv(16)
            if new_msg:
                # print("new msg len:", msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg

            if len(full_msg)-HEADERSIZE == msglen:
                d = pickle.loads(full_msg[HEADERSIZE:])
                print(d)
                new_msg = True
                full_msg = b''
    # try:
    #     move = int(input('Move: '))
    #     while (move != -1):
    #         if (move == 0): gripperClose()
    #         if (move == 1): gripperOpen()
    #         if (move == 2): moveLeft()
    #         if (move == 3): moveRight()
    #         if (move == 4): moveUp()
    #         if (move == 5): moveDown()
    #         if (move == 6): sleep()
    #         if (move == 7): home()
    #         move = int(input('Move: '))
    #     sleep()

    # except Exception as e:
    #     print(e)
    #     sleep()


if __name__ == '__main__':
    main()
