# ✈️ Airline Reservation System (Streamlit + C++)

A full-stack **Airline Reservation System** built primarily in **Python using Streamlit** for a modern web interface, with core backend logic implemented in **C++**.

This hybrid project simulates real-world flight booking systems — allowing users to **book/cancel tickets**, **select seats**, **choose meals**, and **manage reservations** through an intuitive browser-based UI.

---
## 🔗 Live Demo

👉 [Click here to try the app online] ([https://your-streamlit-app-url.streamlit.app](https://airlines-reservation-system-4gmyjmcyshx4oriyfroava.streamlit.app/))

## 🌐 Web Preview (Python Streamlit App)

> ✅ Main Interface — Book, Cancel, and View Reservations  
> ✅ Powered by Python (Streamlit) for fast, interactive UI  
> ✅ Uses Pandas for managing booking data  
> ✅ Optional C++ CLI backend included for offline/terminal use

---

## 📁 Folder Structure

airline-reservation-system/
│
├── Python_Version/ # 🌐 Python Streamlit Web App
│ ├── ARSpy.py # Main Streamlit UI
│ └── requirements.txt # Python dependencies
│
├── CPP_Version/ # 🖥️ Optional: C++ CLI Backend
│ └── main.cpp
│
├── README.md
---
## 🔧 Features

### 🟢 Python (Streamlit) Features
- 🧾 Book, cancel, and view tickets via clean UI
- 🪑 Visual seat layout (available vs booked)
- 🥗 Select food preferences (Veg / Non-Veg / No Food)
- 📊 Display all passenger details in tabular form
- ✅ Real-time feedback and smooth interaction

### 🟡 C++ Backend (Optional CLI version)
- Object-oriented structure with linked list for passengers
- Booking logic, seat management, and meal tracking
- Ideal for understanding core data structures

---

## 🛠️ Tech Stack

| Language     | Frameworks/Tools |
|--------------|------------------|
| C++          | STL, OOP         |
| Python       | Streamlit, Pandas|
| Version Ctrl | Git, GitHub      |

## 🚀 How to Run

### 🔹 Run Python Streamlit App
1. Clone the repository  
   `git clone https://github.com/yourusername/airline-reservation-system.git`
2. Navigate to the Python app  
   `cd airline-reservation-system/Python Version`
3. Install dependencies  
   `pip install -r requirements.txt`
4. Launch the app  
   `streamlit run ARSpy.py`
### 🔹Run C++ Console Version

cd cpp
g++ main.cpp -o airline
./airline

## 🔄 C++ vs Python Features

| Feature             | C++ Console App     | Python Streamlit App |
|---------------------|---------------------|------------------------|
| Booking Tickets     | ✅                  | ✅                     |
| Cancel Reservation  | ✅                  | ✅                     |
| Modify Seat         | ✅                  | ✅                     |
| UI/UX               | ❌ (Text only)      | ✅ (Web Interface)     |
| Data Export         | ❌                  | ✅ (CSV support)       |


