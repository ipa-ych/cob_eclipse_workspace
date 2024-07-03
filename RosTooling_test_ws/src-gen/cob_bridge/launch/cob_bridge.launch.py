from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***

  # *** ROS 2 nodes ***
  teleop = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="teleop",
    remappings=[
      ("joint_states", "joint_state_pub")]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(teleop)

  return ld
