import pyautogui,time
time.sleep(5)
pyautogui.click()   
print("start scroll")
pyautogui.scroll(100000, pause=2)
pyautogui.scroll(-1000, pause=2)
print("stop scroll")
