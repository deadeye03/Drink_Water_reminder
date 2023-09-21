from plyer import notification
import time
import win32com.client as wincom

voice=wincom.Dispatch("SAPI.sPvoice")
voice.rate=0
voice.volume=40

def drink_water_reminder():
    while(True):
         notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink water!",
            app_name="Water Reminder",
            timeout=10
        )
         voice.Speak(f" hey SAURABH It's time to drink water . Continue Hard work After Drink Water")
         time.sleep(900)
if __name__=="__main__":
     drink_water_reminder()
