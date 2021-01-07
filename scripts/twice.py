#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data
   
    if(n>=0 and n<=70):
        print('N normal unti')

    if(n<=90 and n>=71):
        print('R silver unti')

    if(n<=99 and n>=91):
        print('SR golden unti')

    if(n==100):
        print('SSR rainbow unti')
        


rospy.init_node('twice')
sub = rospy.Subscriber('count_up',Int32,cb)
pub = rospy.Publisher('twice',Int32,queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
