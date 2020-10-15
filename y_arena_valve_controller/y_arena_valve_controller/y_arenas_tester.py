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

from y_arena_interfaces.msg import ArenaValves

import random

class YArenasTester(Node):

    def __init__(self):
        super().__init__('y_arenas_tester')
        self.publisher_ = self.create_publisher(ArenaValves, '/arena_valves_open', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.arena = 0
        self.arena_count = 16
        self.valve_count = 3
        self.cycle = 0
        self.cycle_count = 3
        self.valves_open_cycle_0 = [2,2,2]
        self.valves_open_cycle_1 = [0,0,0]

    def timer_callback(self):
        msg = ArenaValves()
        msg.arena = self.arena
        if self.cycle = 0:
            msg.valves = self.valves_open_cycle_0
        elif self.cycle = 1:
            msg.valves = self.valves_open_cycle_1
        else:
            msg.valves = [random.randint(0,self.valve_count-1) for i in range(0,self.valve_count)]
        self.publisher_.publish(msg)
        self.arena += 1
        if self.arena = self.arena_count:
            self.cycle = (self.cycle + 1) % self.cycle_count
            self.arena = 0

def main(args=None):
    rclpy.init(args=args)

    y_arenas_tester = YArenasTester()

    rclpy.spin(y_arenas_tester)

    y_arenas_tester.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
