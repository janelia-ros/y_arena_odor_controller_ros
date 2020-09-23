FROM ros:dashing-ros-base

# Create ROS workspace
COPY . /ws/src/y_arena_valve_controller
WORKDIR /ws

# Use rosdep to install all dependencies
RUN rosdep init && rosdep update && rosdep install --from-paths src -i -y --rosdistro dashing

RUN /bin/bash -c "source /opt/ros/dashing/setup.bash && \
    colcon build --parallel-workers 1 && \
    colcon test --parallel-workers 1"
