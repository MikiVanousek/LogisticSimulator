from pynput import keyboard
from pynput.keyboard import KeyCode

def on_press(key):
    if key == keyboard.Key.up or key == KeyCode.from_char('w'):
        print("up")
    if key == keyboard.Key.down or key == KeyCode.from_char('s'):
        print("down")
    if key == keyboard.Key.left or key == KeyCode.from_char('a'):
        print("left")
    if key == keyboard.Key.right or key == KeyCode.from_char('d'):
        print("right")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()