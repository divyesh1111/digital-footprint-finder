# 🌐 Digital Footprint Finder

A Python tool that checks whether a username exists across multiple popular platforms.  
This project simulates an OSINT-style (Open Source Intelligence) lookup in a simple and educational way.

---

## 🚀 Features

- Search for a username across multiple websites
- Detects whether a profile likely exists
- Color-coded terminal output
- Modular design (easy to add more sites)
- Fast and lightweight

---

## 📁 Project File Structure

```
digital-footprint-finder/
│
├── main.py            # Main program logic
├── sites.py           # List of websites to check
├── requirements.txt   # Required libraries
└── README.md
```

---

## ⚙️ How It Works

1. User enters a username.
2. The script builds profile URLs using templates.
3. It sends HTTP requests to each site.
4. If the response status is `200`, the profile likely exists.
5. Results are displayed in the terminal.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Libraries used:

- `requests` – to send HTTP requests
- `colorama` – for colored terminal output

---

## ▶️ How to Run

```bash
python main.py
```

Then enter the username when prompted.

---

## 🧠 Example Output

```
[FOUND] GitHub: https://github.com/johndoe
[NOT FOUND] Instagram
[FOUND] Reddit: https://www.reddit.com/user/johndoe
```

---

## 🔒 Disclaimer

This tool is for **educational purposes only**.

- It uses only publicly available URLs  
- It does not bypass security  
- It does not collect private data  

Always respect privacy and platform terms of service.

---

## 💡 Possible Improvements

- Multithreading for faster checks
- Export results to CSV
- GUI version
- More platform support
- Profile image detection

---

## 📌 Learning Outcomes

This project demonstrates:

- API/HTTP request handling
- Status code interpretation
- Modular Python design
- File structure organization
- Terminal UI enhancement

---

**Author:** DIVYESH HIRAPARA
**Language:** Python 3
