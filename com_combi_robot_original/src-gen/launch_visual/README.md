# launch_visual

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- robot_state_publisher
- rviz2

The listed nodes offer the following connections:
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: tf_pub_ros2 [tf2_msgs/TFMessage]
- Publisher: tf_static_pub_ros2 [tf2_msgs/TFMessage]
- Publisher: robot_description [std_msgs/String]
- Subscriber: map_sub [nav_msgs/OccupancyGrid]
- Subscriber: robot_description_sub [std_msgs/String]
- Subscriber: inference_result_sub [yolov8_msgs/InferenceResult]

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-cob-slam
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch cob_slam display_robot_0509.launch.py 
```


