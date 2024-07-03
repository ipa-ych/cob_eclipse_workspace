import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution
from launch.event_handlers import OnProcessExit, OnExecutionComplete

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** ROS 1 to ROS 2 bridges ***
  cob_combi_robot_rostooling_ros1_bridge_config = os.path.join(
    get_package_share_directory('cob_combi_robot_rostooling'),
    'config',
    'ros1_bridges.yaml'
  )

  load_bridge_params = ExecuteProcess(
      cmd=['rosparam', 'load', cob_combi_robot_rostooling_ros1_bridge_config]
  )

  ros1_topic_bridge_parameter_bridge = ExecuteProcess(
      cmd=['ros2', 'run', 'ros1_bridge', 'parameter_bridge', '__ns:=bridge_cob_combi_robot_rostooling_topics', '__name:=ros1_topic_bridge_parameter_bridge']
  )
  ros1_service_from_bridge_parameter_bridge = ExecuteProcess(
      cmd=['ros2', 'run', 'ros1_bridge', 'parameter_bridge', '__ns:=bridge_cob_combi_robot_rostooling_from_services', '__name:=ros1_service_from_bridge_parameter_bridge']
  )


  return LaunchDescription([
    RegisterEventHandler(
      event_handler=OnExecutionComplete(
        target_action=load_bridge_params,
        on_completion=[
          LogInfo(msg='Load bridge parameter finished'),
          LogInfo(msg='launching bridge for topics'),
          ros1_topic_bridge_parameter_bridge,
          LogInfo(msg='Start loading bridge parameters')]
      )
    ),
    RegisterEventHandler(
      event_handler=OnExecutionComplete(
        target_action=load_bridge_params,
        on_completion=[
          LogInfo(msg='Load bridge parameter finished'),
          LogInfo(msg='Launching bridge for FROM services'),
          ros1_service_from_bridge_parameter_bridge,
          LogInfo(msg='Start loading bridge parameters')]
      )
    ),
    RegisterEventHandler(
      event_handler=OnExecutionComplete(
        target_action=load_bridge_params,
        on_completion=[
          LogInfo(msg='Load bridge parameter finished'),
          LogInfo(msg='Launching bridge for TO services'),
          ros1_service_to_bridge_parameter_bridge,
          LogInfo(msg='Start loading bridge parameters')]
      )
    ),
    load_bridge_params
  ])
