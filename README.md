
# 🚔 Speeding Fine Calculator - GUI Application

This is a Python GUI application that calculates speeding fines based on user input for speed limits and clocked speed. The program follows a two-tier design:
- **Business Logic Tier** (`speedingfine.py`)
- **Presentation Tier** (`SpeedingTicketGUI-starter.py`)

## 📌 Features

- Calculates fines based on Funnyville's traffic policies:
  - Minimum Fine: $50
  - $5 penalty for each MPH over the limit
  - $200 extra if the driver exceeds the limit by 50+ MPH
- Simple and interactive user interface using `tkinter`
- Error handling for invalid or negative input
- Clear and Exit button functionality

## 🖥️ Technologies Used

- Python 3
- Tkinter (Standard Python GUI library)

## 📁 Files

- `SpeedingTicketGUI-starter.py` – GUI interface (presentation layer)
- `speedingfine.py` – Business logic and fine calculation

## ▶️ How to Run

1. Make sure both `.py` files are in the same directory.
2. Run the GUI:
   ```bash
   python3 SpeedingTicketGUI-starter.py
