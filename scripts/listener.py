import rospy
import espeakng
from std_msgs.msg import String

def test_callback(data):
    rospy.loginfo('received test msg: \"%s\"', data.data)
    espeakng.Speaker().say(data.data)

def listener():
    print('starting gcs vocal listener')

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('vocal/test', String, test_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
