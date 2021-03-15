cmake_minimum_required(VERSION 2.8.3)

project(avatar_r0_5)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

if (CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test/xacro_test.py)
endif (CATKIN_ENABLE_TESTING)
