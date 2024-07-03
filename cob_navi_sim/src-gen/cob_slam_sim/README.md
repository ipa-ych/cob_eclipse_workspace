# cob_slam_sim

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- joy_node
- teleop_twist_joy_node
- twist_mux
- ros2_laserscan_merger
- pointcloud_to_laserscan
- slam_toolbox
- rviz2
- robot_state_publisher
- gazebo
- cob_laserscan
- cob_tricycle_controller
- robot_state_publisher
- cob_joint_state

The listed nodes offer the following connections:
- Publisher: joy_pub [sensor_msgs/Joy]
- Publisher: cmd_vel_pub [geometry_msgs/Twist]
- Subscriber: cmd_vel_sub [geometry_msgs/Twist]
- Publisher: tricycle_controller/cmd_vel [geometry_msgs/Twist]
- Publisher: cloud_in_pub [sensor_msgs/PointCloud2]
- Subscriber: scan_left_sub [sensor_msgs/LaserScan]
- Subscriber: scan_right_sub [sensor_msgs/LaserScan]
- Subscriber: scan_front_sub [sensor_msgs/LaserScan]
- Subscriber: cloud_in_sub [sensor_msgs/PointCloud2]
- Publisher: merged_scan_pub [sensor_msgs/LaserScan]
- Subscriber: map_sub [nav_msgs/OccupancyGrid]
- Subscriber: scan_sub [sensor_msgs/LaserScan]
- Publisher: map_pub [nav_msgs/OccupancyGrid]
- Publisher: tf_pub [tf2_msgs/TFMessage]
- Subscriber: cloud_in [sensor_msgs/PointCloud2]
- Subscriber: map [nav_msgs/OccupancyGrid]
- Subscriber: robot_description_sub [std_msgs/String]
- Subscriber: joint_state [sensor_msgs/JointState]
- Publisher: base_laser_left/scan_raw [sensor_msgs/LaserScan]
- Publisher: base_laser_right/scan_raw [sensor_msgs/LaserScan]
- Publisher: base_laser_front/scan_raw [sensor_msgs/LaserScan]
- Subscriber: tricycle_controller/cmd_vel_sub [geometry_msgs/Twist]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: odom_diff [nav_msgs/Odometry]
- Subscriber: joint_states_sub [sensor_msgs/JointState]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: robot_description [std_msgs/String]
- Publisher: joint_states [sensor_msgs/JointState]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/cob_slam_sim src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch cob_slam_sim cob_slam_sim.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



