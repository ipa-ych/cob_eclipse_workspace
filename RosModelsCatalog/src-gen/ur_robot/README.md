# ur_robot

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- robot_state_publisher_node
- controller_manager
- initial_joint_controller
- initial_joint_controller_spawner_stopped
- ur_ros2_control_node
- dashboard_client
- urscript_interface
- controller_stopper


## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-ur-robot-driver
```


### From source code
```
mkdir -p ros2_ws/src
cd ros2_ws/
git clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Drivergit clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Drivergit clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Drivergit clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```

## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch ur_robot_driver ur_control.launch.py ur_type:= robot_ip:= use_fake_hardware:= initial_joint_controller:= activate_joint_controller:= 
```


