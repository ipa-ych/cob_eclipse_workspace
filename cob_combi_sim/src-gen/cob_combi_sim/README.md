# cob_combi_sim

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- joy_node
- teleop_twist_joy_node
- twist_mux
- ros2_laserscan_merger
- pointcloud_to_laserscan
- slam_toolbox
- rviz2
- yolov8_node
- bt_lifecycle_node
- gazebo
- cob_laserscan
- cob_camera_controller
- cob_tricycle_controller
- cob_torso_controller
- robot_state_publisher
- cob_joint_state
- cob_light_controller
- cob_sound_controller
- cob_mimic_controller
- amcl
- behavior_server
- bt_navigator
- controller_server
- global_costmap
- lifecycle_manager_localization
- lifecycle_manager_navigation
- local_costmap
- map_server
- planner_server
- smoother_server
- velocity_smoother
- waypoint_follower

The listed nodes offer the following connections:
- Publisher: joy_pub [sensor_msgs/Joy]
- Publisher: cmd_vel [geometry_msgs/Twist]
- Subscriber: joy [sensor_msgs/Joy]
- Subscriber: cmd_vel_sub [geometry_msgs/Twist]
- Publisher: tricycle_controller/cmd_vel [geometry_msgs/Twist]
- Subscriber: cmd_vel_navi_sub [geometry_msgs/Twist]
- Publisher: cloud_in [sensor_msgs/PointCloud2]
- Subscriber: base_laser_left/scan_raw/sub [sensor_msgs/LaserScan]
- Subscriber: base_laser_right/scan_raw/sub [sensor_msgs/LaserScan]
- Subscriber: base_laser_front/scan_raw/sub [sensor_msgs/LaserScan]
- Subscriber: cloud_in_sub [sensor_msgs/PointCloud2]
- Publisher: scan [sensor_msgs/LaserScan]
- Subscriber: map_sub_slamtb [nav_msgs/OccupancyGrid]
- Subscriber: scan_sub [sensor_msgs/LaserScan]
- Publisher: map [nav_msgs/OccupancyGrid]
- Publisher: tf [tf2_msgs/TFMessage]
- Subscriber: cloud_in_sub_rviz [sensor_msgs/PointCloud2]
- Subscriber: map_sub [nav_msgs/OccupancyGrid]
- Subscriber: robot_description_sub [std_msgs/String]
- Publisher: Yolov8_Inference [yolov8_msgs/Yolov8Inference]
- Publisher: inference_result [yolov8_msgs/InferenceResult]
- Subscriber: image_raw [sensor_msgs/Image]
- Publisher: base_laser_left/scan_raw [sensor_msgs/LaserScan]
- Publisher: base_laser_right/scan_raw [sensor_msgs/LaserScan]
- Publisher: base_laser_front/scan_raw [sensor_msgs/LaserScan]
- Publisher: torso_left_cam_info [sensor_msgs/CameraInfo]
- Publisher: torso_left_image_raw [sensor_msgs/Image]
- Publisher: torso_left_image_raw_compressed [sensor_msgs/CompressedImage]
- Subscriber: tricycle_controller/cmd_vel_sub [geometry_msgs/Twist]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: odom_diff [nav_msgs/Odometry]
- Subscriber: joint_states_sub [sensor_msgs/JointState]
- Publisher: tf_rsp [tf2_msgs/TFMessage]
- Publisher: tf_static_rsp [tf2_msgs/TFMessage]
- Publisher: robot_description [std_msgs/String]
- Publisher: joint_states [sensor_msgs/JointState]
- ServiceServer: set_Light_color [std_srvs/Trigger]
- ServiceServer: sound_play [cob_srvs/SetString]
- ServiceServer: set_Mimic [std_srvs/Trigger]
- ActionServer: navigate_to_pose [nav2_msgs/NavigateToPose]
- Publisher: cmd_vel_nav [geometry_msgs/Twist]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/cob_combi_sim src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch cob_combi_sim cob_combi_sim.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



