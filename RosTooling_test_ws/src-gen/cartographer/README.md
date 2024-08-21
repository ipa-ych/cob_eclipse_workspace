# cartographer

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- cartographer_node
- cartographer_occupancy_grid_node

The listed nodes offer the following connections:
- Subscriber: scan_cart [sensor_msgs/LaserScan]
- Subscriber: odom_cart [nav_msgs/Odometry]

## Installation

### Using release

To launch this system there is already an existing package that contains the launch file.

The package can be easily installed with the following command:

```
sudo apt install ros-ROSDISTRO-turtlebot3-cartographer
```



## Usage

To launch this system there is already an existing package that contains the launch file. It can be started by:

```
ros2 launch turtlebot3_cartographer cartographer.launch.py 
```


