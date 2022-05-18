

import tkinter as tk



class Stopwatch(tk.Frame):

    def __init__(self, window=None):
        super().__init__(window)
        self.time_label = None
        self.update_time = ""
        self.running = False
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.pack()
        self.create_widgets()
        self.start_button = None
        self.pause_button = None
        self.reset_button = None

    # defining method for creating widgets
    def create_widgets(self):

        # creating a label to display time
        self.time_label = tk.Label(self,
                                   text="00:00:00",
                                   font=('Courier new', 140),
                                   fg="#545869")

        self.time_label.pack()

        # creating different buttons
        self.start_button = tk.Button(self,
                                      text="Start /\n Resume",
                                      height=4,
                                      width=12,
                                      font=("Courier new", 30),
                                      bg="#545869",
                                      fg="#b1b3ba",
                                      activebackground="#529c5c",
                                      command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=12, pady=5)

        self.pause_button = tk.Button(self,
                                      text="Pause",
                                      height=4,
                                      width=12,
                                      font=("Courier new", 30),
                                      bg="#545869",
                                      fg="#b1b3ba",
                                      activebackground="#b84844",
                                      command=self.pause)
        self.pause_button.pack(side=tk.LEFT, pady=5)

        self.reset_button = tk.Button(self,
                                      text="Reset",
                                      height=4,
                                      width=12,
                                      font=("Courier new", 30),
                                      bg="#545869",
                                      fg="#b1b3ba",
                                      activebackground="#3c85c9",
                                      command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=12, pady=5)

    # method for working of start/resume button
    def start(self):

        if not self.running:
            self.time_label.after(1000)
            self.update()
            self.running = True

    # method for working of pause button
    def pause(self):

        if self.running:
            self.time_label.after_cancel(self.update_time)
            self.running = False

    # method for working of reset button
    def reset(self):

        if self.running:
            self.time_label.after_cancel(self.update_time)
            self.running = False
        self.hour, self.minute, self.second = 0, 0, 0
        self.time_label.config(text="00:00:00")

    # method for working of watch
    def update(self):

        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        hour_str = f"{self.hour}" if self.hour > 9 else f"0{self.hour}"
        minute_str = f"{self.minute}" if self.minute > 9 else f"0{self.minute}"
        second_str = f"{self.second}" if self.second > 9 else f"0{self.second}"
        self.time_label.config(text=hour_str + ':' + minute_str + ':' + second_str)
        self.update_time = self.time_label.after(1000, self.update)


# creating main window
root = tk.Tk()
root.title("Stopwatch")

# object declaration
app = Stopwatch(window=root)

# running of main loop
app.mainloop()
