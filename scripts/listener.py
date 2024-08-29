import rospy
import espeakng
from std_msgs.msg import String

def test_callback(data):
    rospy.loginfo('received test msg: \"%s\"', data.data)
    espeakng.Speaker().say(data.data)

def listener():
    rospy.init_node('gcs_vocal', anonymous=True)
    rospy.loginfo('starting gcs vocalizer listener')

    rospy.Subscriber('vocal/test', String, test_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
