import pyautogui

im = pyautogui.screenshot(region=(0, 0, 800, 600))
print(im.getpixel((100, 300)))
