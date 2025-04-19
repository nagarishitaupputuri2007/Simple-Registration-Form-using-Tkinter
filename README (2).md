
# 📝 Simple Registration Form using Tkinter

## 📋 Description
This is a Python-based desktop application that allows users to register their details — First Name, Last Name, and Mobile Number — using a simple graphical interface built with Tkinter. When the "Submit" button is clicked, the entered data is saved to a CSV file named `first.csv`. If the file does not exist, it is created along with appropriate column headers.

## 🚀 Features
- Clean and user-friendly GUI using Tkinter
- Saves user data in a structured CSV format
- Automatically creates `first.csv` if it doesn't exist
- Displays success messages using `messagebox`
- Custom app icon support with `cal.png`

## 🛠️ Setup Instructions

1. **Clone or download the repository**
2. **Make sure you have Python 3.x installed**
3. **Place your custom icon file**  
   Save your icon image as `cal.png` in the same directory as the Python script.

4. **Run the script**
   ```bash
   python your_script_name.py
   ```

> ✅ All registration data will be saved in `first.csv` in the same directory.



## 📂 Example Output in `first.csv`:
```csv
Fname,Lname,Mobile
John,Doe,9876543210
Jane,Smith,9123456780
```
