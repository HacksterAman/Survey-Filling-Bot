import pyautogui

def click(loc):
    pyautogui.moveTo(loc[0], loc[1])
    pyautogui.click()

while True:
    select = pyautogui.locateCenterOnScreen("Select.png", confidence=.9)
    if select!=None:
        click(select)
        while True:
            average = pyautogui.locateCenterOnScreen("Average.png", confidence=.9)
            if average!=None:
                click(average)
                break
        
