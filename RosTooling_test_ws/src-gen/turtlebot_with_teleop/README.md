# turtlebot_with_teleop

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- teleop_key
- gazebo
- robot_state_publisher
- turtlebot3_joint_state
- turtlebot3_diff_drive
- turtlebot3_imu
- camera_driver
- turtlebot3_laserscan

The listed nodes offer the following connections:
- Publisher: cmd_vel_pub [geometry_msgs/Twist]
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

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/turtlebot_with_teleop src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch turtlebot_with_teleop turtlebot_with_teleop.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



