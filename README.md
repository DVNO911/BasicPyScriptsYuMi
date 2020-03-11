# Description

This is a repository for giving a simulation of ABB YuMi simple commands.


## Contents

Currently contains:
Some scripts for sending velocities or angles to interface

Work in Progress:
Service node that can compute Inverse Kinematics


## Installation Guide
This guide is meant for students with no prior experience in using ROS or YuMi.
The main package which will be used to simulate YuMi is this one :
https://github.com/kth-ros-pkg/yumi
However, installation guidelines do not seem to be completely up to date, so here is an alternate method(which includes the installation of the CTH package aswell).
This guide, once complete will be added to the cth_yumi repository aswell.


Install Ros(Melodic) and follow basic user tutorials to get an understanding of how the operative system works.


The Industrial Core packages and ABB packages have to be installed. Source these to your main ROS installation. Then, use the command rospack list-names to check that the following packages are installed:

abb_driver
abb_irb2400_moveit_config
abb_irb2400_moveit_plugins
abb_irb2400_support
abb_irb4400_support
abb_irb5400_support
abb_irb6600_support
abb_irb6640_moveit_config
abb_irb6640_support
abb_resources
industrial_deprecated
industrial_msgs
industrial_robot_client
industrial_robot_simulator
industrial_trajectory_filters

Create the YuMi workspace:

```bash
mkdir -p yumi_depends_ws/src
cd yumi_depends_ws/src
catkin_init_workspace
cd ..
catkin_make
echo "export YUMI_WS='$(pwd)'" >> ~/.bashrc
echo "source $(pwd)/devel/setup.bash" >> ~/.bashrc
```

Clone the Yumi Workspace

```bash
bash
cd $YUMI_WS/src
git clone https://github.com/kth-ros-pkg/yumi.git
git clone https://github.com/DVNO911/BasicPyScriptsYuMi.git
git clone https://github.com/DVNO911/cth_yumi.git
```

Run rosdep to resolve dependencies

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build(This might fail, if it does proceed to next step)

```bash
catkin_make -DCMAKE_BUILD_TYPE=Release
```


Check that you are sourcing the correct branch

```bash
cd $YUMI_WS
rm -rf build/ devel/
cd src/
rm -rf yumi
git clone https://github.com/kth-ros-pkg/yumi.git
cd yumi
git checkout origin/<branch_name>
cd $YUMI_WS
catkin_make -DCMAKE_BUILD_TYPE=Release
```

Build again. You might run into some additional problems but if you manage to build the package then the worst is over :)
The potential problems regard (I believe) some pointers in the URDF/Xacro and/or the necessity of the hector_xacro_tools package. 

## Usage

The yumi package from the KTH repository offers launch files that start a simulation of YuMi which runs Gazebo in the background. There are different kinds, that allow sending in desired angles or velocities. For example:

```bash
roslaunch yumi_launch yumi_gazebo_pos_control.launch
```

or 

```bash
roslaunch yumi_launch yumi_gazebo_vel_control.launch
```

will open up RViz and run the simulation. Now you can run some of the scripts found in the BasicPyScriptsYuMi repository. For example, in the position controlled simulation, try running

```bash
rosrun basic_py_scripts dab.py
```

In the velocity controlled simulation, you can try

```bash
rosrun basic_py_scripts simple_vel.py
```

Please note that the simulation doesnt always launch correctly, so restarting it a couple times might be necessary to make this work.

