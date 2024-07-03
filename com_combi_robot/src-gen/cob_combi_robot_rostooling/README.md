# cob_combi_robot_rostooling

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- joy_node
- twist_mux
- teleop_twist_joy_node
- slam_toolbox
- bt_lifecycle_node
- image_decompress
- yolov8_node
- robot_state_publisher
- rviz2
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
- Publisher: /base/twist_controller/command [geometry_msgs/Twist]
- Subscriber: cmd_vel_sub [geometry_msgs/Twist]
- Subscriber: joy [sensor_msgs/Joy]
- Publisher: cmd_vel [geometry_msgs/Twist]
- Subscriber: map_sub_slamtb [nav_msgs/OccupancyGrid]
- Subscriber: scan_sub [sensor_msgs/LaserScan]
- Publisher: map [nav_msgs/OccupancyGrid]
- Publisher: tf [tf2_msgs/TFMessage]
- ServiceClient: setLightGreen [std_srvs/Trigger]
- ServiceClient: setLightRed [std_srvs/Trigger]
- ServiceClient: setLightCyan [std_srvs/Trigger]
- ServiceClient: setLightCyanBreath [std_srvs/Trigger]
- ServiceClient: setLightCyanSweep [std_srvs/Trigger]
- ServiceClient: setMimicBusy [std_srvs/Trigger]
- ServiceClient: setMimicAsking [std_srvs/Trigger]
- ServiceClient: setMimicBlinking [std_srvs/Trigger]
- ServiceClient: /sound/play [cob_srvs/SetString]
- Subscriber: /torso_cam3d_left_upright/rgb/image_raw/compressed [sensor_msgs/CompressedImage]
- Publisher: cam_left/decompressed [sensor_msgs/Image]
- Publisher: Yolov8_Inference [yolov8_msgs/Yolov8Inference]
- Publisher: inference_result [yolov8_msgs/InferenceResult]
- Subscriber: image_raw [sensor_msgs/Image]
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: tf_pub_ros2 [tf2_msgs/TFMessage]
- Publisher: tf_static_pub_ros2 [tf2_msgs/TFMessage]
- Publisher: robot_description [std_msgs/String]
- Subscriber: map_sub [nav_msgs/OccupancyGrid]
- Subscriber: robot_description_sub [std_msgs/String]
- Subscriber: inference_result_sub [yolov8_msgs/InferenceResult]
- Subscriber: tf_sub [tf2_msgs/TFMessage]
- Subscriber: tf_static_sub [tf2_msgs/TFMessage]
- ActionServer: navigate_to_pose_as [nav2_msgs/NavigateToPose]
- Publisher: cmd_vel_nav [geometry_msgs/Twist]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/cob_combi_robot_rostooling src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch cob_combi_robot_rostooling cob_combi_robot_rostooling.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



