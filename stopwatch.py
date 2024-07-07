import tkinter as tk
from tkinter import ttk
import time

def draw_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height

    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

def update_time():
    if running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 100) % 100)
        time_string = f"{minutes:02}:{seconds:02}:{milliseconds:02}"
        time_label_var.set(time_string)
    root.after(10, update_time)

def start():
    global running, start_time
    if not running:
        start_time = time.time() - elapsed_time
        running = True

def stop():
    global running, elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        running = False

def reset():
    global start_time, elapsed_time
    start_time = time.time()
    elapsed_time = 0
    time_label_var.set("00:00:00")

root = tk.Tk()
root.title("Stopwatch with Gradient Background")
root.geometry("600x400")

gradient_canvas = tk.Canvas(root, width=600, height=400)
gradient_canvas.pack(fill="both", expand=True)

root.update_idletasks()  
draw_gradient(gradient_canvas, "#ffcccc", "#cc99ff")

frame = ttk.Frame(gradient_canvas)
frame.place(relx=0.5, rely=0.5, anchor="center")

time_label_var = tk.StringVar(value="00:00:00")
time_label = ttk.Label(frame, textvariable=time_label_var, font=("Helvetica", 48))
time_label.pack(pady=10)


start_button = ttk.Button(frame, text="Start", command=start)
start_button.pack(side="left", padx=5)

stop_button = ttk.Button(frame, text="Stop", command=stop)
stop_button.pack(side="left", padx=5)

reset_button = ttk.Button(frame, text="Reset", command=reset)
reset_button.pack(side="left", padx=5)

start_time = 0
elapsed_time = 0
running = False

update_time()

root.mainloop()
