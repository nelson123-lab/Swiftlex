from pynput.mouse import Listener

with Listener() as listener:
    listener.join()

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass
