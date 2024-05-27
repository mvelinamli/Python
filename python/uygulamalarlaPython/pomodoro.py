import time
import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.duration = 25 * 60  # Varsayılan çalışma süresi (25 dakika)
        self.remaining_time = self.duration
        self.is_running=False

        self.timer_label = tk.Label(self.master, text="", font=("Helvetica",48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.master, command=self.start_timer, text="Start" )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Durdur", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)


    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.run_timer()

    def stop_timer(self):
        self.is_running = False

    def run_timer(self):
        if self.is_running and self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.remaining_time -= 1
            self.master.after(1000, self.run_timer)
        elif self.remaining_time == 0:
            self.timer_label.config(text="Pomodoro Tamamlandı!")
            self.is_running = False
            self.remaining_time = self.duration

def main():
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()