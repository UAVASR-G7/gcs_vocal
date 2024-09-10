import rospy
import espeakng
from std_msgs.msg import String
from std_msgs.msg import Bool

def test_callback(data):
    rospy.loginfo('received test msg: \"%s\"', data.data)
    espeakng.Speaker().say(data.data)

def landing_callback(data):
    if data.data: # bool is True
        rospy.loginfo('received landing msg: \"%s\"', data.data)
        espeakng.Speaker().say('Landing complete')

def listener():
    rospy.init_node('gcs_vocal', anonymous=True)
    rospy.loginfo('starting gcs vocalizer listener')

    rospy.Subscriber('vocal/test', String, test_callback)
    rospy.Subscriber('vocal/land', Bool, test_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
