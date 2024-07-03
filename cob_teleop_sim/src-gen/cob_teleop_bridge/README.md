# cob_teleop_bridge

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- joy_node
- twist_mux
- teleop_twist_joy_node
- gazebo
- robot_state_publisher
- cob_joint_state

The listed nodes offer the following connections:
- Publisher: cmd_vel_out [geometry_msgs/Twist]
- Subscriber: cmd_vel_sub [geometry_msgs/Twist]
- Publisher: cmd_vel_pub [geometry_msgs/Twist]
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: joint_states [sensor_msgs/JointState]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/cob_teleop_bridge src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch cob_teleop_bridge cob_teleop_bridge.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



