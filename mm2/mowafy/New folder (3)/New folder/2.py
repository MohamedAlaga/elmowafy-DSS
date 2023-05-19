import tkinter as tk
import pickle
import numpy as np
from tkinter import messagebox
# Create main window
root = tk.Tk()
root.title("Dataset Columns")
root.geometry("600x500")
root.configure(bg='#333333')
# Define the columns
from tkinter import messagebox


frame = tk.Frame(bg='#333333')

battery_power_label = tk.Label(
    frame, text="battery_power", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
battery_power_entry = tk.Entry(frame, font=("Arial", 16))

blue_label = tk.Label(
    frame,text="blue",bg='#333333', fg="#FFFFFF", font=("Arial", 16))
blue_entry = tk.Entry(frame,font=("Arial",16))

###############




clock_speed_label = tk.Label(
    frame, text="clock_speed", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
clock_speed_entry = tk.Entry(frame, font=("Arial", 16))

dual_sim_label = tk.Label(
    frame, text="dual_sim", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
dual_sim_entry = tk.Entry(frame, font=("Arial", 16))


fc_label = tk.Label(
    frame, text="fc", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
fc_entry = tk.Entry(frame, font=("Arial", 16))

four_g_label = tk.Label(
    frame, text="four_g", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
four_g_entry = tk.Entry(frame, font=("Arial", 16))

int_memory_label = tk.Label(
    frame, text="int_memory", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
int_memory_entry = tk.Entry(frame, font=("Arial", 16))


m_dep_label = tk.Label(
    frame, text="m_dep", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
m_dep_entry = tk.Entry(frame, font=("Arial", 16))

mobile_wt_label = tk.Label(
    frame, text="mobile_wt", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
mobile_wt_entry = tk.Entry(frame, font=("Arial", 16))

n_cores_label = tk.Label(
    frame, text="n_cores", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
n_cores_entry = tk.Entry(frame, font=("Arial", 16))


pc_label = tk.Label(
    frame, text="pc", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
pc_entry = tk.Entry(frame, font=("Arial", 16))

px_height_label = tk.Label(
    frame, text="px_height", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
px_height_entry = tk.Entry(frame, font=("Arial", 16))

px_width_label = tk.Label(
    frame, text="px_width", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
px_width_entry = tk.Entry(frame, font=("Arial", 16))

ram_label = tk.Label(
    frame, text="ram", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
ram_entry = tk.Entry(frame, font=("Arial", 16))
sc_h_label = tk.Label(
    frame, text="sc_h", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
sc_h_entry = tk.Entry(frame, font=("Arial", 16))
sc_w_label = tk.Label(
    frame, text="sc_w", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
sc_w_entry = tk.Entry(frame, font=("Arial", 16))
talk_time_label = tk.Label(
    frame, text="talk_time", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
talk_time_entry = tk.Entry(frame, font=("Arial", 16))
three_g_label = tk.Label(
    frame, text="three_g", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
three_g_entry = tk.Entry(frame, font=("Arial", 16))
touch_screen_label = tk.Label(
    frame, text="touch_screen", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
touch_screen_entry = tk.Entry(frame, font=("Arial", 16))
wifi_label = tk.Label(
    frame, text="wifi", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
wifi_entry = tk.Entry(frame, font=("Arial", 16))

#
def check ():
     battery_power=float(battery_power_entry.get())
     blue=float(blue_entry.get())
     clock_speed=float(clock_speed_entry.get())
     dual_sim=float(dual_sim_entry.get())
     fc=float(fc_entry.get())
     four_g=float(four_g_entry.get())
     int_memory=float(int_memory_entry.get())
     m_dep=float(m_dep_entry.get())
     mobile_wt=float(mobile_wt_entry.get())
     n_cores=float(n_cores_entry.get())
     pc=float(pc_entry.get())
     px_height=float(px_height_entry.get())
     px_width=float(px_width_entry.get())
     ram=float(ram_entry.get())
     sc_h=float(sc_h_entry.get())
     sc_w=float(sc_w_entry.get())
     talk_time=float(talk_time_entry.get())
     three_g=float(three_g_entry.get())
     touch_screen=float(touch_screen_entry.get())
     wifi=float(wifi_entry.get())
     t=np.array([[battery_power,blue,clock_speed,dual_sim,fc,
           four_g,int_memory,m_dep, mobile_wt,n_cores,
           pc, px_height, px_width, ram,sc_h,sc_w,
           talk_time,three_g,touch_screen,wifi]])
     filename = 'Price_Regression_Model.pkl'        
     loaded_model = pickle.load(open(filename,"rb"))
     y_pred = loaded_model.predict(t)
     print("Predicted Value: ", y_pred) 
     messagebox.showinfo(y_pred)


check_button = tk.Button(
    frame, text="check", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),command=check)


battery_power_label.grid(row=1, column=0)
battery_power_entry.grid(row=1, column=1, pady=20)

blue_label.grid(row=1, column=2)
blue_entry.grid(row=1, column=3, pady=20)

clock_speed_label.grid(row=2, column=0)
clock_speed_entry.grid(row=2, column=1, pady=20)


dual_sim_label.grid(row=2, column=2)
dual_sim_entry.grid(row=2, column=3, pady=20)


fc_label.grid(row=3, column=0)
fc_entry.grid(row=3, column=1, pady=20)


four_g_label.grid(row=3, column=2)
four_g_entry.grid(row=3, column=3, pady=20)


int_memory_label.grid(row=4, column=0)
int_memory_entry.grid(row=4, column=1, pady=20)


m_dep_label.grid(row=4, column=2)
m_dep_entry.grid(row=4, column=3, pady=20)


mobile_wt_label.grid(row=5, column=0)
mobile_wt_entry.grid(row=5, column=1, pady=20)


n_cores_label.grid(row=5, column=2)
n_cores_entry.grid(row=5, column=3, pady=20)


pc_label.grid(row=6, column=0)
pc_entry.grid(row=6, column=1, pady=20)


px_height_label.grid(row=6, column=2)
px_height_entry.grid(row=6, column=3, pady=20)


px_width_label.grid(row=7, column=0)
px_width_entry.grid(row=7, column=1, pady=20)


ram_label.grid(row=7, column=2)
ram_entry.grid(row=7, column=3, pady=20)


sc_h_label.grid(row=8, column=0)
sc_h_entry.grid(row=8, column=1, pady=20)


sc_w_label.grid(row=8, column=2)
sc_w_entry.grid(row=8, column=3, pady=20)


talk_time_label.grid(row=9, column=0)
talk_time_entry.grid(row=9, column=1, pady=20)


three_g_label.grid(row=9, column=2)
three_g_entry.grid(row=9, column=3, pady=20)


touch_screen_label.grid(row=10, column=0)
touch_screen_entry.grid(row=10, column=1, pady=20)


wifi_label.grid(row=10, column=2)
wifi_entry.grid(row=10, column=3, pady=20)

check_button.grid(row=10, column=4, padx=50, pady=30)




frame.pack()
root.mainloop()
