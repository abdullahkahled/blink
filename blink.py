import ctypes
import time
from plyer import notification
# تعين عدد التذكير
reminder_number = 3

#كتباة دالة تنفيذ التذكير 
def blink():
    notification.notify(
    title="blink",
    message ="Blink now"
    )
# حلقة للتذكير بالرمش كل وقت محدد
while True:
    for _ in range (x):
        blink()
        time.sleep(60)
