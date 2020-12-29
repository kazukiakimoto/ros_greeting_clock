#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import datetime
import pytz

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    #now = datetime.datetime.now()
    hour = int(now.strftime('%H'))
    pub.publish(hour)
    rate.sleep()
