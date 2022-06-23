#!../razah-lib/bin/python3
import rospy
from std_msgs.msg import String
import os
print(os.getcwd())
from chatterbot import ChatBot
import speech_recognition as sr
import time

def speech2text():
	# ros
    rospy.init_node('mic', anonymous=True)
    pub = rospy.Publisher('/razah/verbal/text', String, queue_size=10)
    rate = rospy.Rate(10)
    
    # find mic
    while not rospy.is_shutdown():
      r = sr.Recognizer()
      available_devices = sr.Microphone.list_microphone_names()
      if "Maono Elf pro: USB Audio (hw:2,0)" in available_devices:
        available_devices = available_devices.index('Maono Elf pro: USB Audio (hw:2,0)')
        break
      else:
        available_devices = "none"
        print("mic not found")

    # listen
    mic = sr.Microphone(available_devices)
    while not rospy.is_shutdown():
      try:
        with mic as source:
          print("listening ...")
          r.adjust_for_ambient_noise(source, duration=0.2)
          audio = r.listen(source)
        pub.publish(r.recognize_google(audio))
        
       # error handling 
      except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        print("Restarting listening module")
        time.sleep(2)
        # restart listening
        available_devices = sr.Microphone.list_microphone_names()
        if "Maono Elf pro: USB Audio (hw:2,0)" in available_devices:
          available_devices = available_devices.index('Maono Elf pro: USB Audio (hw:2,0)')
          mic = sr.Microphone(available_devices)
      except sr.UnknownValueError:
        print("unknown error occured")
        print("Restarting listening module")
        time.sleep(2)
        # restart listening
        available_devices = sr.Microphone.list_microphone_names()
        if "Maono Elf pro: USB Audio (hw:2,0)" in available_devices:
          available_devices = available_devices.index('Maono Elf pro: USB Audio (hw:2,0)')
          mic = sr.Microphone(available_devices)
	  
      except Exception as e:
        print("Exception occured: ", e)
        print("Restarting listening module")
        time.sleep(2)
        # restart listening
        available_devices = sr.Microphone.list_microphone_names()
        if "Maono Elf pro: USB Audio (hw:2,0)" in available_devices:
          available_devices = available_devices.index('Maono Elf pro: USB Audio (hw:2,0)')
          mic = sr.Microphone(available_devices)

if __name__ == '__main__':
  try:
  	speech2text()
  except rospy.ROSInterruptException: 
    exit()
