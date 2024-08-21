# cob_eclipse_ws
This repository contains RosTooling projects created with RosTooling approach for simulation and read-world scenarios using cob4-25 robot.<br>
For more about RosTooling and model-driven development approach:  [RosTooling](https://github.com/ipa320/RosTooling) <br>
For RosTooling tutorials: 
[RosTooling Tutorials](https://ipa320.github.io/RosTooling.github.io/) <br>
For RosTooling Model Catalog: [Model Catalog](https://github.com/ipa-nhg/RosModelsCatalog)



## Project overview
1. cob_teleop_sim & cob_teleop_robot
- Manual control of robot omnidirectional-base using teleoperation
2. cob_navi_sim & cob_navi_robot
- Mapping and self-navigation using slam_toolbox & nav2 
3. cob_combi_sim & cob_combi_robot
- Integrated scenario with teleoperation, navigation, object detection, HMI and BehaviorTree


## Tips
- UML graphs are created with <project_name>_uml.rossystem fles. The graphs can be found under [/RosTooling_Visualization](https://github.com/ipa-ych/cob_eclipse_workspace/tree/main/RosTooling_Visualization)
- To launch the auto-generated ROS2 packages (under <project_name>/src-gen), dependencies and external packages are required. Please refer to https://github.com/ipa-ych/YCH_ros2_ws
