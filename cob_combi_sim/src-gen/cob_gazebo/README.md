# cob_gazebo

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
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

The listed nodes offer the following connections:
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

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-cob-sim-trad
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch cob_sim_trad cob_gazebo.launch.py 
```


