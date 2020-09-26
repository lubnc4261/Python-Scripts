import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import psutil
import platform
from datetime import datetime

win=tk.Tk()

win.title("Task Manager")

win.geometry("650x500")

win.resizable(True, True)

def _quit():
    win.quit()
    win.destroy()
    exit()


tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Settings")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="System")
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="CPU")


tabControl.pack(expand=1, fill="both")

stg = ttk.LabelFrame(tab1, text="Settings")
stg.grid(column=0, row=0, padx=20, pady=20)
labeltab1 = ttk.Label(stg, text="Colour")
labeltab1.grid(column=0, row=1, sticky="W")


sys = ttk.LabelFrame(tab2, text="System Informations")
uname = platform.uname()
sys.grid(column=0, row=0, padx=20, pady=20)

labeltab1 = ttk.Label(sys, text=f"System: {uname.system}")
labeltab1.grid(column=0, row=0, sticky="W")
labeltab2 = ttk.Label(sys, text=f"Node Name: {uname.node}")
labeltab2.grid(column=0, row=1, sticky="W")
labeltab3 = ttk.Label(sys, text=f"Release: {uname.release}")
labeltab3.grid(column=0, row=2, sticky="W")
labeltab4 = ttk.Label(sys, text=f"Version: {uname.version}")
labeltab4.grid(column=0, row=3, sticky="W")
labeltab5 = ttk.Label(sys, text=f"Machine: {uname.machine}")
labeltab5.grid(column=0, row=4, sticky="W")
labeltab6 = ttk.Label(sys, text=f"Processor: {uname.processor}")
labeltab6.grid(column=0, row=5, sticky="W")

cpu = ttk.LabelFrame(tab3, text="CPU Informations")
cpufreq = psutil.cpu_freq()
cpu.grid(column=0, row=0, padx=20, pady=20)
labeltab1 = ttk.Label(cpu, text=f"Max Frequency: {cpufreq.max:.2f}Mhz")
labeltab1.grid(column=0, row=0, sticky="W")
labeltab2 = ttk.Label(cpu, text=f"Min Frequency: {cpufreq.min:.2f}Mhz")
labeltab2.grid(column=0, row=1, sticky="W")
labeltab3 = ttk.Label(cpu, text=f"Current Frequency: {cpufreq.current:.2f}Mhz")
labeltab3.grid(column=0, row=2, sticky="W")
































































win.mainloop()
