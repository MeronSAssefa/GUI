# Name: Meron Assefa
# Class: AI240
# Date: JUNE 16,2024
# Description: GUI program for calculating speeding fines based on town policy.

import tkinter as tk
from tkinter import messagebox
from speedingfine import SpeedingFineCalculator # type: ignore

class SpeedingFineFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Business logic object
        self.speedingFineCalculator = SpeedingFineCalculator()

        # Variables for Entry widgets
        self.speedLimitVar = tk.DoubleVar()
        self.clockedSpeedVar = tk.DoubleVar()
        self.fineVar = tk.DoubleVar()

        # Initialize the GUI components
        self.initComponents()

    def initComponents(self):
        self.initMainFrame()
        self.initButtonsFrame()

    def initMainFrame(self):
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, padx=10, pady=10)

        # Labels and Entry boxes
        tk.Label(main_frame, text="Speed Limit:").grid(row=0, column=0, sticky='e')
        tk.Entry(main_frame, textvariable=self.speedLimitVar).grid(row=0, column=1)

        tk.Label(main_frame, text="Clocked Speed:").grid(row=1, column=0, sticky='e')
        tk.Entry(main_frame, textvariable=self.clockedSpeedVar).grid(row=1, column=1)

        tk.Label(main_frame, text="Speeding Fine:").grid(row=2, column=0, sticky='e')
        fine_entry = tk.Entry(main_frame, textvariable=self.fineVar, state='readonly')
        fine_entry.grid(row=2, column=1)

    def initButtonsFrame(self):
        buttons_frame = tk.Frame(self)
        buttons_frame.grid(row=1, column=0, pady=10)

        # Buttons
        tk.Button(buttons_frame, text="Calculate", command=self.calculateFine).grid(row=0, column=0, padx=5)
        tk.Button(buttons_frame, text="Clear", command=self.clear).grid(row=0, column=1, padx=5)
        tk.Button(buttons_frame, text="Exit", command=self.exit).grid(row=0, column=2, padx=5)

    def calculateFine(self):
        try:
            speed_limit = self.speedLimitVar.get()
            clocked_speed = self.clockedSpeedVar.get()

            if speed_limit <= 0 or clocked_speed <= 0:
                raise ValueError("Speeds must be positive")

            self.speedingFineCalculator.speedingLimit = speed_limit
            fine = self.speedingFineCalculator.calculateSpeedingFine(clocked_speed)

            self.fineVar.set(fine)

        except Exception:
            messagebox.showerror("Error", "Please enter valid positive numbers")
            self.clear()

    def clear(self):
        self.speedLimitVar.set(0.0)
        self.clockedSpeedVar.set(0.0)
        self.fineVar.set(0.0)

    def exit(self):
        self.quit()

# main method
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Speeding Fine Calculator of Funnyville")
    app = SpeedingFineFrame(root)
    app.pack()
    root.mainloop()

