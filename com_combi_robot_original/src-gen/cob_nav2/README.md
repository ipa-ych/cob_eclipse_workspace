# cob_nav2

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
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
- Subscriber: tf_sub [tf2_msgs/TFMessage]
- Subscriber: tf_static_sub [tf2_msgs/TFMessage]
- ActionServer: navigate_to_pose_as [nav2_msgs/NavigateToPose]
- Publisher: cmd_vel_nav [geometry_msgs/Twist]

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
ros2 launch cob_sim_trad cob_navi_only.launch.py 
```


