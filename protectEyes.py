



import time
import ctypes

user32 = ctypes.windll.User32




def waitUntilUnlock():
    time.sleep(1)
    OpenDesktop = user32.OpenDesktopA
    SwitchDesktop = user32.SwitchDesktop
    DESKTOP_SWITCHDESKTOP = 0x0100
    while 1:
      hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
      result = SwitchDesktop (hDesktop)
      if result:
        print "Unlocked"
        break
      else:
        print time.asctime (), "still locked"
        time.sleep (2)

    
duration = 30 * 60 # 20 minute
# duration = 5
while True:
    time.sleep(duration)    
    user32.LockWorkStation()

    waitUntilUnlock()


