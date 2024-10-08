import rospy
import espeakng
from threading import Lock
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from spar_msgs.msg import TargetLocalisation

mutex = Lock()

def test_callback(msg):
    global mutex
    with mutex:
        rospy.loginfo("received test msg: '%s'" % msg.data)
        espeakng.Speaker().say(msg.data)

def landing_callback(msg):
    global mutex
    with mutex:
        if msg.data:  # bool is True
            rospy.loginfo("received landing msg")
            espeakng.Speaker().say("Landing complete")

def aruco_callback(msg):
    global mutex
    with mutex:
        rospy.loginfo("received aruco id: '%d'" % msg.data)
        espeakng.Speaker().say("Detected aruco marker with ID %d" % msg.data)

def target_callback(msg):
    rospy.loginfo("received target of type: '%s'" % msg.target_label)
    espeakng.Speaker().say(
        "%s found at %.1f in X and %.1f in Y"
        % (msg.target_label, msg.frame_x, msg.frame_y)
    )

def listener():
    rospy.init_node("gcs_vocal", anonymous=True)
    rospy.loginfo("starting gcs vocalizer listener")

    rospy.Subscriber("vocal/test", String, test_callback)
    rospy.Subscriber("vocal/land", Bool, landing_callback)
    rospy.Subscriber("vocal/aruco", Int32, aruco_callback)
    rospy.Subscriber(
        "target_detection/localisation", TargetLocalisation, target_callback
    )

    rospy.spin()

if __name__ == "__main__":
    listener()
