import rospy
import espeakng
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int32

def test_callback(msg):
    rospy.loginfo("received test msg: '%s'" % msg.data)
    espeakng.Speaker().say(msg.data)

def landing_callback(msg):
    if msg.data: # bool is True
        rospy.loginfo("received landing msg")
        espeakng.Speaker().say('Landing complete')

def aruco_callback(msg):
    rospy.loginfo("received aruco id: '%d'" % msg.data)
    espeakng.Speaker().say("Detected aruco marker with ID %d" % msg.data)

def listener():
    rospy.init_node('gcs_vocal', anonymous=True)
    rospy.loginfo('starting gcs vocalizer listener')

    rospy.Subscriber('vocal/test', String, test_callback)
    rospy.Subscriber('vocal/land', Bool, landing_callback)
    rospy.Subscriber('vocal/aruco', Int32, aruco_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
