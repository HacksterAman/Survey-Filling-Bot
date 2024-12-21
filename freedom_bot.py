import pyautogui
import time

def click(loc):
    print(f"Clicking at location: {loc}")
    pyautogui.moveTo(loc[0], loc[1])
    pyautogui.click()

while True:
    try:
        print("Searching for 'Select.png'...")
        select = pyautogui.locateCenterOnScreen("Select.png", confidence=0.9)
        if select is not None:
            click(select)
            time.sleep(0.1)
            while True:
                print("Searching for 'Average.png'...")
                average = pyautogui.locateCenterOnScreen("Average.png", confidence=0.9)
                if average is not None:
                    click(average)
                    break
        else:
            print("'Select.png' not found. Retrying...")
        #time.sleep(1)  # Adding a small delay to prevent rapid looping
    except pyautogui.ImageNotFoundException:
        print("ImageNotFoundException: Could not locate the image.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
