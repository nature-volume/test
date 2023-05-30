import pyautogui
import time

while True:

    # 等待3秒钟，确保当前窗口为活动窗口
    time.sleep(3)

    # 按下方向键
    pyautogui.press('esc')

    # 释放方向键
    pyautogui.press('esc', presses=0, interval=0)

    time.sleep(10)