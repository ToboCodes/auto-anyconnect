import pyautogui
import time
wait = 0.2
user = 'ccontrerasc@entel.cl'
auth = 'Gponinstalador@147'
pin = '46267'

cli = pyautogui.getActiveWindow()
cli.minimize()
# Launch VPN from desktop icon.
pyautogui.moveTo(38, 223, duration=wait)
pyautogui.doubleClick()
# Input username and password.
while not pyautogui.pixelMatchesColor(1405, 760, (0, 103, 184)):
    time.sleep(wait)
pyautogui.write(user + "\n")
while not pyautogui.pixelMatchesColor(1363, 812, (0, 103, 184)):
    time.sleep(wait)
pyautogui.write(auth + "\n")
while not pyautogui.pixelMatchesColor(1285, 807, (253, 253, 253)):
    time.sleep(wait)
# Click VPN "Accept" button.
pyautogui.moveTo(1301, 801, duration=wait)
pyautogui.click()
# Launch X-Lite from desktop icon.
pyautogui.moveTo(109, 232, duration=wait)
pyautogui.doubleClick()
# Launch Soft-phone from desktop icon.
pyautogui.moveTo(187, 224, duration=wait)
pyautogui.doubleClick()
# Click Soft-phone "Open" button.
while not pyautogui.pixelMatchesColor(1659, 243, (92, 92, 92)):
    time.sleep(wait)
pyautogui.moveTo(1638, 243, duration=wait)
pyautogui.click()
# Click Login at Point(x=1362, y=15)
while not pyautogui.pixelMatchesColor(745, 50, (0, 128, 0)):
    time.sleep(wait)
pyautogui.moveTo(1362, 15, duration=wait)
pyautogui.click()
# Input PIN 46267
pyautogui.write(pin)
# Service selector at Point(x=1261, y=164)
pyautogui.moveTo(1261, 164, duration=wait)
pyautogui.click()
# Service MAT2 at Point(x=1249, y=178)
pyautogui.moveTo(1249, 178, duration=wait)
pyautogui.click()
# Accept button at Point(x=1321, y=201)
pyautogui.moveTo(1321, 201, duration=wait)
pyautogui.click()
time.sleep(wait)
pyautogui.click()
