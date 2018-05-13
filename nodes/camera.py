#!/usr/bin/env python
from __future__ import print_function

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy
from openag_brain.peripherals.camera import Camera

if __name__ == "__main__":
    rospy.init_node("sensor_camera")
    image_pub = rospy.Publisher('aerial_image/image_raw', Image, queue_size=10)
    bridge = CvBridge()
    r = rospy.Rate(24)

    with Camera() as camera:
        while not rospy.is_shutdown():
            cv2_image = camera.capture()
            try:
                image_pub.publish(bridge.cv2_to_imgmsg(cv2_image, 'rgb8'))
            except CvBridgeError as e:
                print(e)

            r.sleep()
