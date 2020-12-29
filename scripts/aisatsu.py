#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def cb(message):
    if message.data < 5:
        rospy.loginfo("%d時です。こんな時間に何しているんですか？", message.data)
    elif message.data < 10:
        rospy.loginfo("%d時です。おはようございます", message.data)
    elif message.data < 19:
        rospy.loginfo("%d時です。こんにちわ", message.data)
    else:
        rospy.loginfo("%d時です。こんばんわ", message.data)

if __name__ == '__main__':
    rospy.init_node('aisatsu')
    pub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
