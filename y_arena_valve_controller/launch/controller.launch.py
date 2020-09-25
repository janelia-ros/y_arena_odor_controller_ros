import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='y_arena_valve_controller', node_executable='controller', output='screen',
            node_name='y_arena_valve_controller'),
    ])
