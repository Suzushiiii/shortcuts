import time
import threading
from random import randrange
from pynput.mouse import Button
from pynput.mouse import Controller as MauseControler
from pynput.keyboard import Controller as KeyboardControler
from pynput.keyboard import Listener, KeyCode, Key


delay = 20
button = Button.left
key_down = Key.down
key_enter = Key.enter
start_stop_key = KeyCode(char='s')
exit_key = Key.esc

class ClickMause(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.key_down = key_down
        self.key_enter = key_enter
        self.running = False
        self.program_running = True
    
    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False
    
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:

                randx = randrange(680, 1416)
                randy = randrange(325, 803)

                t = time.localtime()
                cur = time.strftime('%I:%M:%S %p', t)

                print("Moving mouse to pos: {} {} // {}".format(randx, randy, cur))

                mouse.position = (randx, randy, t)
                time.sleep(self.delay)
                    # mouse.position = (2015, 241)
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # mouse.position = (1836, 791)
                    # mouse.click(self.button)
                    # time.sleep(self.delay)


                    # mouse.position = (1806, 524)
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # keyboard.press(self.key_enter)
                    # keyboard.release(self.key_enter)
                    # mouse.position = (1827, 835)
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # keyboard.press(self.key)
                    # keyboard.release(self.key)
                    # time.sleep(self.delay)


                    # mouse.position = (1445, 846) # group
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # mouse.position = (1450, 278) # select group
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # mouse.position = (1364, 472) # rm group
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # keyboard.press(self.key_enter) # enter
                    # keyboard.release(self.key_enter)
                    # mouse.position = (1384, 812) # close
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # mouse.position = (1832, 840) # close 2
                    # mouse.click(self.button)
                    # time.sleep(self.delay)
                    # keyboard.press(self.key_down) # press down
                    # keyboard.release(self.key_down)
                    # time.sleep(self.delay)
                    


mouse = MauseControler()
keyboard = KeyboardControler()
click_thread = ClickMause(delay, button)
click_thread.start()
print("")
print("Press 's' to start script!")


def on_press(key): 
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()

        elif key == exit_key:
            print("Stoping mouse :D")
            click_thread.exit()
            listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()