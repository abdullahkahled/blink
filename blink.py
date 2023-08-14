import ctypes
import time
from plyer import notification
# تعين عدد التذكير
x = 3

#كتباة دالة تنفيذ التذكير 
def blink():
    notification.notify(
    title="تنبيه",
    message ="قم بالرمش الآن"
    )
# حلقة للتذكير بالرمش كل وقت محدد
while True:
    for _ in range (x):
        blink()
        time.sleep(60)