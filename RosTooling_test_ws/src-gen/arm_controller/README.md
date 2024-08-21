# arm_controller

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- arm_controller

The listed nodes offer the following connections:
- Subscriber: arm_controller/joint_trajectory [trajectory_msgs/JointTrajectory]
- ActionServer: arm_controller/follow_joint_trajectory [control_msgs/FollowJointTrajectory]
- Publisher: arm_controller/state [control_msgs/JointTrajectoryControllerState]

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-open-manipulator-x-controller
```


### From source code
```
mkdir -p ros2_ws/src
cd ros2_ws/
git clone https://github.com/ROBOTIS-GIT/open_manipulator -b humble-devel
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```

## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch open_manipulator_x_controller open_manipulator_x_controller.launch.py 
```


