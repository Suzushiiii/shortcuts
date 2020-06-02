import ctypes
import time
import re
from ctypes import wintypes
from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener

def fix_string(s, **changes):
    changes = dict((re.escape(k), v) for k, v in changes.items())
    pattern = re.compile("|".join(changes.keys()))
    return pattern.sub(lambda m: changes[re.escape(m.group(0))], sExit)

def shorten_tip(message):
    ms_len = 50
    if len(message) > ms_len:
        last = message[:ms_len].strip()[-1]
        special = [",", "/"]
        if last in special:
            return message[:ms_len].replace(last, "").strip() + '...'
        return message[:ms_len].strip() + '...'
    return message

kbd = Controller()
t = 0.02
t_minimize = 1
tip = 'Use {} to type "{}"'
s1 = "q+`"
s2 = "q+;"
s3 = "q+'"
s4 = "q+/"
s5 = "q+1"
s6 = "q+2"
s7 = "q+3"
sExit = "<Shift>+<Esc>"
ch = {"<": " ", ">": " "}
sExit_fixed = fix_string(sExit, **ch)

t1 = "Wersja 1-2 (aktualna), Brak błędów."
t2 = "Wersja 1-2 (aktualna), W sprawozdaniu są następujące błędy:"
t3 = "Wersja 1-0 (nieaktualna)."
t4 = "Cześć, timsheetami, godzinami pracy, nadgodzinami, zajmuje się kontroling, napisz na controlling@pkfpolska.pl."
t5 = "Zaakceptuj mi logowanie, za chwilę."
t6 = "link do połączenia."
t7_placeholder = "Dostaliśmy proces odebrania uprawnień dla {}, podczas nadawanie uprawniień została również ustawiona data ich odebrania.\
Proces generuje się automatycznie.\r\nCzy mam zablokować konto z dniem {}?"

tip_text = {s1: t1, s2: t2, s3: t3, s4: t4, s5: t5, s6: t6, s7: t7_placeholder}

print('')
print('Welcome')
print('Use shortcuts to type things.')
print('')
print('=========Use {} to stop script========='.format(sExit_fixed.strip()))
print('')

for k, v in tip_text.items():
    print(tip.format(k.replace("", " ")[1:-1], shorten_tip(v)))

list_of = []
for k, v in tip_text.items():
    list_of.extend([k[0],k[-1]])
list_of = list(set(list_of))

def remove_shortcut_text():
    for i in range(2):
        kbd.press(Key.backspace)
        kbd.release(Key.backspace)
    for k in list_of:
        kbd.release(k)

def press_buttons(c):
    kbd.press(c)
    kbd.release(c)
    time.sleep(t)
    

def activate_12_good():
    remove_shortcut_text()
    for c in t1:
        press_buttons(c)

def activate_12_bad():
    remove_shortcut_text()
    for c in t2:
        press_buttons(c)

def activate_10():
    remove_shortcut_text()
    for c in t3:
        press_buttons(c)

def ts_control():
    remove_shortcut_text()
    for c in t4:
        press_buttons(c)

def g2a():
    remove_shortcut_text()
    for c in t5:
        press_buttons(c)

def link_g2a():
    remove_shortcut_text()
    for c in t6:
        press_buttons(c)

def odebranie_up():
    remove_shortcut_text()
    worker_name = input("Wprowadź nazwę Pracownika:")
    due_date = input("Wprowadź datę wyłączena konta:")
    t7 = t7_placeholder.format(worker_name, due_date)
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    user32.ShowWindow(h_wnd, 6)
    time.sleep(t_minimize)
    for c in t7:
        press_buttons(c)

def stop_script():
    h.stop()


with keyboard.GlobalHotKeys({
        s1: activate_12_good,
        s2: activate_12_bad,
        s3: activate_10,
        s4: ts_control,
        s5: g2a,
        s6: link_g2a,
        s7: odebranie_up,
        sExit: stop_script}) as h:
    h.join()