# turtlebot_gazebo

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- gazebo
- robot_state_publisher
- turtlebot3_joint_state
- turtlebot3_diff_drive
- turtlebot3_imu
- camera_driver
- turtlebot3_laserscan

The listed nodes offer the following connections:
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: joint_states [sensor_msgs/JointState]
- Subscriber: cmd_vel_diff [geometry_msgs/Twist]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: odom_diff [nav_msgs/Odometry]
- Publisher: imu [sensor_msgs/Imu]
- Publisher: camera_info [sensor_msgs/CameraInfo]
- Publisher: image_raw [sensor_msgs/Image]
- ServiceServer: set_camera_info [sensor_msgs/SetCameraInfo]
- Publisher: scan_turtlebot [sensor_msgs/LaserScan]

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-turtlebot3-gazebo
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py 
```


