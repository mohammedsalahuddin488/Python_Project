import time
from plyer import notification

while True:
    print("Please Drink water")
    notification.notify(title= "water reminder", message= "please drink water")
    time.sleep(60*60)  # Wait for 1 hour before sending the next reminder