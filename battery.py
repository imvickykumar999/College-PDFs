
import psutil, time, os
from pygame import mixer

i = 0
battery = psutil.sensors_battery()

plugged = battery.power_plugged
percent = battery.percent

maxbat = [97, percent+1][0]
minbat = [40, percent-1][0]

alarm = 1  # sec

if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"

status = str(percent) + '% | ' + plugged
print(status)

count, data = 0, []

while True:
    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent

    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"

    count += 1
    i += 1

    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', plugged, str(battery))
    time.sleep(60)

    if percent >= maxbat or percent <= minbat:
        os.system('audio.mp3')
        time.sleep(alarm)
    continue
