import ctypes
import time
import re
import os
from ctypes import wintypes
from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener

class ShortCuts:
    def __init__(self):
        super(ShortCuts, self).__init__()
        title = "Background Shortcuts"
        os.system('title ' + title)
        os.system('color 30')
        self.kbd = Controller()
        self.t = 0.02
        self.t_minimize = 1
        tip = 'Use {} to type "{}"'
        self.s1 = "q+`"
        self.s2 = "q+;"
        self.s3 = "q+'"
        self.s4 = "q+/"
        self.s5 = "q+1"
        self.s6 = "q+2"
        self.s7 = "q+3"
        self.sExit = "<Shift>+<Esc>"
        ch = {"<": " ", ">": " "}
        sExit_fixed = self.fix_string(self.sExit, **ch)

        self.t1 = "Wersja 1-2 (aktualna), Brak błędów."
        self.t2 = "Wersja 1-2 (aktualna), W sprawozdaniu są następujące błędy:"
        self.t3 = "Wersja 1-0 (nieaktualna)."
        self.t4 = "Cześć, timsheetami, godzinami pracy, nadgodzinami, zajmuje się kontroling, napisz na controlling@pkfpolska.pl."
        self.t5 = "Zaakceptuj mi logowanie, za chwilę."
        self.t6 = "link do połączenia."
        self.t7_placeholder = "Dostaliśmy proces odebrania uprawnień dla {}, podczas nadawania uprawnień została również ustawiona data ich odebrania. \
Proces generuje się automatycznie.\rCzy mam zablokować konto z dniem {}?"

        self.tip_text = {self.s1: self.t1, self.s2: self.t2, self.s3: self.t3, self.s4: self.t4, self.s5: self.t5, self.s6: self.t6, self.s7: self.t7_placeholder}

        print('')
        print('Welcome')
        print('Use shortcuts to type things.')
        print('')
        print('=========Use {} to stop script========='.format(sExit_fixed.strip()))
        print('')

        for k, v in self.tip_text.items():
            print(tip.format(k.replace("", " ")[1:-1], self.shorten_tip(v)))

        self.list_of = []
        for k, v in self.tip_text.items():
            self.list_of.extend([k[0],k[-1]])
        self.list_of = list(set(self.list_of))

    def minimize(self):
        user32 = ctypes.windll.user32
        h_wnd = user32.GetForegroundWindow()
        user32.ShowWindow(h_wnd, 6)

    def fix_string(self, s, **changes):
        changes = dict((re.escape(k), v) for k, v in changes.items())
        pattern = re.compile("|".join(changes.keys()))
        return pattern.sub(lambda m: changes[re.escape(m.group(0))], self.sExit)

    def shorten_tip(self, message):
        ms_len = 50
        if len(message) > ms_len:
            last = message[:ms_len].strip()[-1]
            special = [",", "/"]
            if last in special:
                return message[:ms_len].replace(last, "").strip() + '...'
            return message[:ms_len].strip() + '...'
        return message

    def remove_shortcut_text(self):
        for i in range(2):
            self.kbd.press(Key.backspace)
            self.kbd.release(Key.backspace)
        for k in self.list_of:
            self.kbd.release(k)

    def press_buttons(self, c):
        self.kbd.press(c)
        self.kbd.release(c)
        time.sleep(self.t)
        

    def activate_12_good(self):
        self.remove_shortcut_text()
        for c in self.t1:
            self.press_buttons(c)

    def activate_12_bad(self):
        self.remove_shortcut_text()
        for c in self.t2:
            self.press_buttons(c)

    def activate_10(self):
        self.remove_shortcut_text()
        for c in self.t3:
            self.press_buttons(c)

    def ts_control(self):
        self.remove_shortcut_text()
        for c in self.t4:
            self.press_buttons(c)

    def g2a(self):
        self.remove_shortcut_text()
        for c in self.t5:
            self.press_buttons(c)

    def link_g2a(self):
        self.remove_shortcut_text()
        for c in self.t6:
            self.press_buttons(c)

    def odebranie_up(self):
        self.remove_shortcut_text()
        worker_name = input("Wprowadź nazwę Pracownika:")
        due_date = input("Wprowadź datę wyłączena konta:")
        t7 = self.t7_placeholder.format(worker_name, due_date)
        self.minimize()
        time.sleep(self.t_minimize)
        for c in t7:
            self.press_buttons(c)

    def stop_script(self):
        h.stop()

if __name__ == "__main__":
    sc = ShortCuts()
    sc.minimize()
    with keyboard.GlobalHotKeys({
            sc.s1: sc.activate_12_good,
            sc.s2: sc.activate_12_bad,
            sc.s3: sc.activate_10,
            sc.s4: sc.ts_control,
            sc.s5: sc.g2a,
            sc.s6: sc.link_g2a,
            sc.s7: sc.odebranie_up,
            sc.sExit: sc.stop_script}) as h:
        h.join()