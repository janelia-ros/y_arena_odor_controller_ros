ARG FROM_IMAGE=ros:dashing
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# copy overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
COPY . .

# copy manifests for caching
WORKDIR /opt
RUN mkdir -p /tmp/opt && \
    find ./ -name "package.xml" | \
      xargs -I '{}' cp '{}' --parents -t /tmp/opt && \
    find ./ -name "requirements.txt" | \
      xargs -I '{}' cp '{}' --parents -t /tmp/opt && \
    find ./ -name "COLCON_IGNORE" | \
      xargs -I '{}' cp '{}' --parents -t /tmp/opt || true

# multi-stage for building
FROM $FROM_IMAGE AS builder

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
COPY --from=cacher /tmp/$OVERLAY_WS/src ./src
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && \
    apt-get install -y \
        python3-pip && \
    find ./ -name "requirements.txt" | \
      xargs -I '{}' pip3 install -r '{}' && \
    rosdep install -y \
      --from-paths \
        src \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
COPY --from=cacher $OVERLAY_WS/src ./src
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

# run launch file
CMD ["ros2", "launch", "y_arena_valve_controller", "controller.launch.py"]
