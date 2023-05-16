import pyHook 
import pythoncom 
 
def onclick(event): 
    print event.Position 
    return True 
 
hm = pyHook.HookManager() 
hm.SubscribeMouseAllButtonsDown(onclick) 
hm.HookMouse() 
pythoncom.PumpMessages() 
hm.UnhookMouse() 

"""
https://www.quora.com/How-do-I-detect-mouse-events-left-click-with-Python
"""