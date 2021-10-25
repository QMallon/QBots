import pyautogui
##From KIANBROSE and canklot
im1 = pyautogui.screenshot(region=(0,0,800,650))
im1.save(r"./savedimage.png")