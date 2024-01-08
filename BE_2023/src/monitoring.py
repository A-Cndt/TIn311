import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import time
import random

class IHM_Monitoring(object):
    def __init__(self, root, num_instruments=6):
        self.root = root
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.num_instruments = num_instruments
        self.x_values = [[] for _ in range(self.num_instruments)]
        self.y_values = [[] for _ in range(self.num_instruments)]
        self.lines = [self.ax.plot([], [])[0] for _ in range(self.num_instruments)]

    def plot(self, x, y, instr):
        if 1 <= instr <= self.num_instruments:
            self.x_values[instr - 1].append(x)
            self.y_values[instr - 1].append(y)

    def update(self, frame):
        for instr, line in enumerate(self.lines):
            line.set_data(self.x_values[instr], self.y_values[instr])
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def animate(self):
        self.animation = FuncAnimation(self.fig, self.update, frames=100, interval=100)

    def start(self):
        self.thread = threading.Thread(target=self.animate)
        self.thread.start()

# Example usage:
root = tk.Tk()
monitoring_ui = IHM_Monitoring(root, num_instruments=6)
monitoring_ui.start()
