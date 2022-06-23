#!../tent/src/razah/razah-lib/bin/python3
import rospy
from std_msgs.msg import String
import pyttsx3

engine = pyttsx3.init()
def say(text):
    print(text)
    engine.say(text.data)
    engine.runAndWait()

def text2speech():
    rospy.init_node('text2speech', anonymous=True)
    rate = rospy.Rate(10)
    rospy.Subscriber("/razah/verbal/speech", String, say)
    rospy.spin()

if __name__ == '__main__':
    try:
    	text2speech()
    except rospy.ROSInterruptException: 
        exit()
