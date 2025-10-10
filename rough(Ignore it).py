import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
import ctypes

# ---- SETTINGS ----
WORK_MIN = 40  # session length in minutes
BAR_HEIGHT = 10
LOG_FILE = "Car game/focus_log.txt"

# ---- WINDOWS CLICK-THROUGH ATTEMPT ----
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20

def make_clickthrough(hwnd):
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT)

# ---- MAIN APP ----
class FocusTimer:
    def __init__(self, root):
        self.root = root
        root.title("Ghost Focus Timer")
        root.geometry(f"{root.winfo_screenwidth()}x{BAR_HEIGHT}+0+0")
        root.overrideredirect(True)  # remove window frame
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.6)  # semi-transparent

        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        make_clickthrough(hwnd)

        self.canvas = tk.Canvas(root, height=BAR_HEIGHT, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.width = root.winfo_screenwidth()
        self.bar = self.canvas.create_rectangle(0, 0, self.width, BAR_HEIGHT, fill="green", outline="")

        self.seconds = WORK_MIN * 60
        self.streak = self.load_streak()
        self.update_bar()
        threading.Thread(target=self.countdown).start()

    def update_bar(self):
        ratio = self.seconds / (WORK_MIN * 60)
        self.canvas.coords(self.bar, 0, 0, self.width * ratio, BAR_HEIGHT)
        if ratio > 0.5:
            color = "green"
        elif ratio > 0.2:
            color = "yellow"
        else:
            color = "red"
        self.canvas.itemconfig(self.bar, fill=color)
        self.root.update()

    def countdown(self):
        while self.seconds > 0:
            time.sleep(1)
            self.seconds -= 1
            self.update_bar()
        self.done_popup()

    def done_popup(self):
        self.streak += 1
        self.save_streak()
        messagebox.showinfo("Done! 🎉", f"Session complete!\n🔥 Current streak: {self.streak} sessions")
        self.root.destroy()

    def load_streak(self):
        if not os.path.exists(LOG_FILE):
            return 0
        with open(LOG_FILE, "r") as f:
            try:
                return int(f.read())
            except:
                return 0

    def save_streak(self):
        with open(LOG_FILE, "w") as f:
            f.write(str(self.streak))


root = tk.Tk()
app = FocusTimer(root)
root.mainloop()
