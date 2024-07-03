# my_awesome_system

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- node1
- node2
- node1a
- node2a

The listed nodes offer the following connections:
- Publisher: my_publisher [std_msgs/Bool]
- ServiceServer: my_server [std_srvs/Empty]
- ActionServer: my_act_server [control_msgs/JointTrajectory]
- Subscriber: my_subscriber [std_msgs/Bool]
- ServiceClient: my_client [std_srvs/Empty]
- ActionClient: my_act_client [control_msgs/JointTrajectory]
- Publisher: other_publisher [std_msgs/Bool]
- Subscriber: other_subscriber [std_msgs/Bool]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/my_awesome_system src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch my_awesome_system my_awesome_system.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



