# UWRegistrationBot by Sonnhi Duong

## Overview
**UWRegistrationBot** is a Python-based tool that automatically registers for classes at the University of Washington.  
The bot takes your login information, class codes, and registration time.  

One minute before your specified registration time, it opens a browser and loads your inputs. Roughly 3 seconds before registration, the bot repeatedly clicks the submit button to maximize the chance of successful enrollment.  

This project was developed as a personal Python project using libraries such as **Selenium** and **PySimpleGUI**.  
**Use at your own risk.**

---

## Installation
1. Download the repository ZIP file and extract its contents.  
2. Run the `Driver` executable located in the `dist` folder.  

---

## Usage
1. Launch the program; a UI window will appear.  
2. Enter your UW Student account login information.  
3. Fill in the class codes under **SLN**, and add any add codes if applicable.  
4. The **Credit** column is optional and should only be used for variable-credit classes.  
5. Use the dropdown menu to select the correct registration time.  
6. Double-check all information before starting; incorrect inputs will prevent registration.  

Once running, the window will close automatically and reopen when registration time approaches. The program can run in the background while you continue other tasks.  

---

## Contributing
Contributions are welcome! Areas for improvement include:  
- Testing and debugging  
- Enhancing the GUI  
- Adding more flexible registration date inputs  
