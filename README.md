# YATA - Yet Another Terminal Application

## Screenshot
![Screenshot](Screenshot.png)

## Overview

**YATA** is a lightweight, Python-based terminal emulator built with **CustomTkinter**. It allows users to run:

- CMD commands  
- PowerShell commands  
- Scoop-installed binaries  
- Any executable available in your system PATH  

All inside a clean, modern GUI with semi-transparent windows and read-only output.  

---

## Features

- Minimalist and responsive **GUI** using CustomTkinter  
- Runs any **system command** from CMD/PowerShell  
- Captures **stdout** and **stderr** safely  
- Cleans **ANSI escape codes** for readable output  
- Read-only output with editable input  
- Optional instructions label that disappears after first command  

---

## Installation

1. Make sure you have **Python 3.10+** installed.  
2. Install the required module:

```bash
pip install customtkinter
```
3. Download the YATA.py script.

## Usage

1. Run YATA:

```bash
python YATA.py
```

2. Type your command in the input box and press Enter.
3. The output will appear in the main textbox.
### Examples:
```text
> dir
> fastfetch
```
**Notes**

- Python commands can be executed via python <file> or by modifying the script to add inline Python evaluation.

- ANSI-colored output is cleaned for readability, so some color formatting from tools like Fastfetch may not appear.

- Output is read-only; input is editable only in the input box.

- Semi-transparent GUI with customizable theme using CustomTkinter.

## License

This project is licensed under the MIT License.

© 2025 CoolGuy158-Git
