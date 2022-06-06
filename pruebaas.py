from interbotix_xs_modules.locobot import InterbotixLocobotXS

# This script makes the end-effector go to a specific pose by defining the pose components
#
# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200'
# Then change to this directory and type 'python ee_pose_components.py'

def main():
    locobot = InterbotixLocobotXS("locobot_wx250s", "mobile_wx250s")
    # locobot.arm.go_to_home_pose()
    # locobot.arm.set_ee_pose_components(x=0.0, y=0.1, z=0.0, roll=0.1, pitch=1.0)
    # locobot.arm.set_ee_pose_components(x=0.1, z=0.2)
    # locobot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # locobot.arm.set_ee_pose_components(x=0.2, z=0.2)
    

    #newhome
    locobot.arm.set_ee_pose_components(x=0.3, y=0.0 ,z=0.35)
    locobot.arm.set_ee_pose_components(x=0.3, y=-0.2 ,z=0.47)
    locobot.arm.set_ee_pose_components(x=0.3, y=-0.2 ,z=0.1)
    locobot.arm.set_ee_pose_components(x=0.3, y=0.2 ,z=0.1)
    locobot.arm.set_ee_pose_components(x=0.3, y=0.2 ,z=0.47)

    # locobot.arm.set_ee_pose_components(x=0.46, y=0.2 ,z=0.35)
    # locobot.arm.set_ee_pose_components(x=0.46, y=-0.2 ,z=0.35)





if __name__=='__main__':
    main()