import time

answer()
wait(100)

callerName = "Honk"
if currentCall.network == "SIP":
    callerName = currentCall.callerName;
else:
    callerName = "Alien"

say("Hello " + str(currentCall.callerName) + " and welcome! Please stand by while I try to connect the central speaker system. Just a second.")
wait(1000)
say("Connection established. I will announce your call and then patch you directly to the central speaker system. Please be ready for your announcement!")
startCallRecording("{{ webhook_uri }}", {"format":"audio/mp3"})
wait(500)
say("Hello c base crew. This is Tropo speaking. I received a call from " + callerName + " and here is the message:")
wait(10000)
stopCallRecording()
say("Thank you. Your time is up")
hangup()