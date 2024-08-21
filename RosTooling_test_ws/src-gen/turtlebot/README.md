# turtlebot

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- turtlebot_node
- turtlebot3_laserscan
- robot_state_publisher

The listed nodes offer the following connections:
- Subscriber: cmd_vel [geometry_msgs/Twist]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: odom [nav_msgs/Odometry]
- Publisher: scan [sensor_msgs/LaserScan]
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-turtlebot3-bringup
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch turtlebot3_bringup robot.launch.py 
```


