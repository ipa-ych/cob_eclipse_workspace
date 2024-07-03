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


## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-cob-sim
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch cob_sim cob_navi.launch.py 
```


