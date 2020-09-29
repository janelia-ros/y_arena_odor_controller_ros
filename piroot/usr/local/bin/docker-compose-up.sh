#!/bin/bash

if [[ -e "/dev/arena/0" &&
      -e "/dev/arena/1" &&
      -e "/dev/arena/2" &&
      -e "/dev/arena/3" &&
      -e "/dev/arena/4" &&
      -e "/dev/arena/5" &&
      -e "/dev/arena/6" &&
      -e "/dev/arena/7" &&
      -e "/dev/arena/8" &&
      -e "/dev/arena/9" &&
      -e "/dev/arena/10" &&
      -e "/dev/arena/11" &&
      -e "/dev/arena/12" &&
      -e "/dev/arena/13" &&
      -e "/dev/arena/14" &&
      -e "/dev/arena/15" ]]; then
  echo "/usr/bin/docker-compose -f /home/yuser/y_arena_valve_controller_ros/docker-compose.yml up -d"
  /usr/bin/docker-compose -f /home/yuser/y_arena_valve_controller_ros/docker-compose.yml up -d
fi
