import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = round(weight / (height ** 2), 2)  
    result_label.config(text=f"Your BMI is {bmi}")

root = tk.Tk()
root.title("BMI Calculator")

height_label = tk.Label(root, text="Enter your height (in meters):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Enter your weight (in kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop() 
