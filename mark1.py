import socket
from interbotix_xs_modules.locobot import InterbotixLocobotXS



flagPosition = False
xaxis = 0.46
yaxis = 0
zaxis = 0.35

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
    global yaxis
    global zaxis
    
    if yaxis<0.2:
        yaxis = yaxis+0.05
        locobot.arm.set_ee_pose_components(x=0.46, y=yaxis ,z=zaxis)


def moveRight():
    global yaxis
    global zaxis
    
    if yaxis>-0.2:
        yaxis = yaxis-0.05
        locobot.arm.set_ee_pose_components(x=0.46, y=yaxis ,z=zaxis)



# def moveFront():
#     val = float(input('X: '))
#     locobot.arm.set_ee_cartesian_trajectory(x=val)


# def moveBack():
#     val = float(input('X: ')) * -1
#     locobot.arm.set_ee_cartesian_trajectory(x=val)


def moveUp():
    global yaxis
    global zaxis
    
    if zaxis<0.46:
        zaxis = zaxis+0.02
        locobot.arm.set_ee_pose_components(x=0.46, y=yaxis ,z=zaxis)


def moveDown():
    global yaxis
    global zaxis
    
    if zaxis>0.1:
        zaxis = zaxis-0.02
        locobot.arm.set_ee_pose_components(x=0.46, y=yaxis ,z=zaxis)


def home():
    locobot.arm.go_to_home_pose()


def sleep():
    locobot.arm.go_to_sleep_pose()


def moveRobot(pose):
    global flagPosition
    try:
        # while (pose != 'double_tap'):
        if (pose == 'fist'):
            gripperClose()
        if (pose == 'fingers_spread'):
            gripperOpen()
        if (pose == 'wave_in'):
            if flagPosition:
                moveLeft()
            else:
                moveDown()    
        if (pose == 'wave_out'):
            if flagPosition:
                moveRight()
            else:
                moveUp()    
        if (pose == 'double_tap'):
            flagPosition = not flagPosition     
            # sleep()
        
        # if (pose == 4):
        #     poseUp()
        # if (pose == 5):
        #     poseDown()
        # if (pose == 6):
        #     sleep()
        # if (pose == 7):
        #     home()
    except Exception as e:
        print(e)

home()

while True:
    while True:
        msg = s.recv(1024).decode('utf-8')
        print(msg, yaxis,zaxis)
        moveRobot(msg)
