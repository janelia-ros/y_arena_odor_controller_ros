#!/bin/bash

if [[ -e "/dev/arena/00" &&
      -e "/dev/arena/01" &&
      -e "/dev/arena/02" &&
      -e "/dev/arena/03" &&
      -e "/dev/arena/04" &&
      -e "/dev/arena/05" &&
      -e "/dev/arena/06" &&
      -e "/dev/arena/07" &&
      -e "/dev/arena/08" &&
      -e "/dev/arena/09" &&
      -e "/dev/arena/10" &&
      -e "/dev/arena/11" &&
      -e "/dev/arena/12" &&
      -e "/dev/arena/13" &&
      -e "/dev/arena/14" &&
      -e "/dev/arena/15" ]]; then
  echo "/usr/bin/docker-compose -f /home/yuser/y_arena_valve_controller_ros/docker-compose.yml up -d"
  /usr/bin/docker-compose -f /home/yuser/y_arena_valve_controller_ros/docker-compose.yml up -d
fi
