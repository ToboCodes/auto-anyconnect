import pyautogui
import time

cli = pyautogui.getActiveWindow()
cli.minimize()
# Open VPN from icon
pyautogui.moveTo(38, 223, duration=0.25)
pyautogui.doubleClick()
# Input user and password
while not pyautogui.pixelMatchesColor(1405, 760, (0, 103, 184)):
    time.sleep(0.3)
pyautogui.write('ccontrerasc@entel.cl\n')
while not pyautogui.pixelMatchesColor(1363, 812, (0, 103, 184)):
    time.sleep(0.3)
pyautogui.write('Gponinstalador@147\n')
while not pyautogui.pixelMatchesColor(1285, 807, (253, 253, 253)):
    time.sleep(0.3)
# VPN "Accept" button at Point(x=1301, y=801)
pyautogui.moveTo(1301, 801, duration=0.25)
pyautogui.click()
# X-Lite icon at Point(x=109, y=232)
pyautogui.moveTo(109, 232, duration=0.25)
pyautogui.doubleClick()
# Soft-phone icon at Point(x=187, y=224)
pyautogui.moveTo(187, 224, duration=0.25)
pyautogui.doubleClick()
# Soft-phone "Open" button at Point(x=1638, y=243)
while not pyautogui.pixelMatchesColor(1659, 243, (92, 92, 92)):
    time.sleep(0.3)
pyautogui.moveTo(1638, 243, duration=0.25)
pyautogui.click()
# Logon at Point(x=1362, y=15)
while not pyautogui.pixelMatchesColor(745, 50, (0, 128, 0)):
    time.sleep(0.3)
pyautogui.moveTo(1362, 15, duration=0.25)
pyautogui.click()
# Input PIN 46267
pyautogui.write('46267')
# Service selector at Point(x=1261, y=164)
pyautogui.moveTo(1261, 164, duration=0.25)
pyautogui.click()
# Service MAT2 at Point(x=1249, y=178)
pyautogui.moveTo(1249, 178, duration=0.25)
pyautogui.click()
# Accept button at Point(x=1321, y=201)
pyautogui.moveTo(1321, 201, duration=0.25)
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
