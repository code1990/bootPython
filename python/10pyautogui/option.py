import pyautogui
# alert
pyautogui.alert(text='This is an alert box.', title='Test')
# option
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# password
a = pyautogui.password('Enter password (text will be hidden)')
print(a)
# prompt
a = pyautogui.prompt('input  message')
print(a)