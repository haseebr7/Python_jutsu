import tkinter as tk
from tkinter import messagebox
import ctypes

# ---- SETTINGS ----
DEFAULT_MINUTES = 20
DEFAULT_BAR_HEIGHT = 30

# ---- WINDOWS CLICK-THROUGH ----
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20

def make_clickthrough(hwnd):
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT)

# ---- GHOST TIMER ----
class GhostTimer:
    def __init__(self, root, minutes=DEFAULT_MINUTES, bar_height=DEFAULT_BAR_HEIGHT):
        self.root = root
        root.title("Ghost Focus Timer")
        root.geometry(f"{root.winfo_screenwidth()}x{bar_height}+0+0")
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.6)

        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        make_clickthrough(hwnd)

        self.canvas = tk.Canvas(root, height=bar_height, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.width = root.winfo_screenwidth()
        self.bar = self.canvas.create_rectangle(0, 0, self.width, bar_height, fill="green", outline="")

        self.minutes = minutes
        self.total_seconds = self.minutes * 60
        self.seconds = self.total_seconds

        self.running = False
        self.paused = False

        # Keyboard shortcuts
        root.bind("<space>", lambda e: self.toggle_pause())
        root.bind("r", lambda e: self.reset())

        self.update_bar()

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.update_timer()

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused
            if not self.paused:
                self.update_timer()

    def reset(self, new_minutes=None):
        self.running = False
        self.paused = False
        if new_minutes:
            self.minutes = new_minutes
        self.total_seconds = self.minutes * 60
        self.seconds = self.total_seconds
        self.update_bar()

    def update_bar(self):
        ratio = self.seconds / self.total_seconds
        self.canvas.coords(self.bar, 0, 0, self.width * ratio, self.canvas.winfo_height())
        if ratio > 0.5:
            color = "green"
        elif ratio > 0.2:
            color = "yellow"
        else:
            color = "red"
        self.canvas.itemconfig(self.bar, fill=color)
        self.root.update()

    def update_timer(self):
        if self.running and not self.paused and self.seconds > 0:
            self.seconds -= 1
            self.update_bar()
            self.root.after(1000, self.update_timer)
        elif self.seconds <= 0:
            self.running = False
            messagebox.showinfo("Done! 🎉", "Session Complete!")
            self.reset()
        elif self.paused:
            self.root.after(1000, self.update_timer)

# ---- CONTROL PANEL ----
class ControlPanel:
    def __init__(self, ghost_timer):
        self.gt = ghost_timer
        self.root = tk.Tk()
        self.root.title("Ghost Timer Control Panel")
        self.root.geometry("300x200")

        tk.Label(self.root, text="Timer Length (minutes):").pack(pady=5)
        self.timer_entry = tk.Entry(self.root)
        self.timer_entry.insert(0, str(DEFAULT_MINUTES))
        self.timer_entry.pack()

        tk.Label(self.root, text="Bar Height (px):").pack(pady=5)
        self.bar_entry = tk.Entry(self.root)
        self.bar_entry.insert(0, str(DEFAULT_BAR_HEIGHT))
        self.bar_entry.pack()

        tk.Button(self.root, text="Start", command=self.start).pack(pady=5)
        tk.Button(self.root, text="Pause/Resume", command=self.gt.toggle_pause).pack(pady=5)
        tk.Button(self.root, text="Reset", command=self.reset).pack(pady=5)

        self.root.mainloop()

    def start(self):
        try:
            minutes = int(self.timer_entry.get())
            self.gt.reset(new_minutes=minutes)
        except:
            self.gt.reset()
        self.gt.start()

    def reset(self):
        try:
            minutes = int(self.timer_entry.get())
            height = int(self.bar_entry.get())
            self.gt.root.geometry(f"{self.gt.width}x{height}+0+0")
            self.gt.reset(new_minutes=minutes)
        except:
            self.gt.reset()

# ---- MAIN ----
if __name__ == "__main__":
    ghost_root = tk.Tk()
    ghost_timer = GhostTimer(ghost_root)
    ControlPanel(ghost_timer)
