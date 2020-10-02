# Copyright (c) 2020, Howard Hughes Medical Institute
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rclpy
from rclpy.node import Node

from pathlib import Path
from modular_client import ModularClients

from y_arena_interfaces.msg import ArenaValves

class YArenaValveController(Node):

    def __init__(self):
        super().__init__('y_arena_valve_controller')
        arena_dev_paths = sorted(Path('/dev/arena').glob('*'))
        arena_dev_ports = [str(p) for p in arena_dev_paths]
        arena_dev_keys = [int(p.name) for p in arena_dev_paths]
        self.devs = ModularClients(use_ports=arena_dev_ports,keys=arena_dev_keys)

        self.arena_valves_open_sub = self.create_subscription(
            ArenaValves,
            '/arena_valves_open',
            self.arena_valves_open_callback,
            10)
        self.arena_valves_open_sub

    def arena_valves_open_callback(self, msg):
        self.get_logger().info('arena_valves_open_callback: arena = {0}, valves = {1}'.format(msg.arena,msg.valves))
        try:
            self.devs[msg.arena].set_valves_open(msg.valves.tolist())
        except (IndexError, OSError) as e:
            pass

def main(args=None):
    rclpy.init(args=args)

    y_arena_valve_controller = YArenaValveController()

    rclpy.spin(y_arena_valve_controller)

    y_arena_valve_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
