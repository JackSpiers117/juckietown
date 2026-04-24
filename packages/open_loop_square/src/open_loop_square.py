#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped


class OpenLoopSquare:

    def __init__(self):
        rospy.init_node("open_loop_square", anonymous=True)

        self.pub = rospy.Publisher(
            "/juckiebot/car_cmd_switch_node/cmd",
            Twist2DStamped,
            queue_size=1
        )

        self.msg = Twist2DStamped()
        rospy.sleep(1)  #allow connection

    def send_cmd(self, v, omega, duration):

        rate = rospy.Rate(10)
        end_time = rospy.Time.now() + rospy.Duration(duration)

        while rospy.Time.now() < end_time and not rospy.is_shutdown():
            self.msg.header.stamp = rospy.Time.now()
            self.msg.v = v
            self.msg.omega = omega
            self.pub.publish(self.msg)
            rate.sleep()

    def stop(self):
        self.send_cmd(0.0, 0.0, 0.5)

    def run_square(self):

        for i in range(4):

            #forward
            self.send_cmd(0.3, 0.0, 1.8)
            self.stop()

            #90 degree turn
            self.send_cmd(0.0, 2.0, 0.55)
            self.stop()

        #final stop
        self.stop()


if __name__ == "__main__":
    node = OpenLoopSquare()
    node.run_square()
