# Importing files from python lib
# tkinter - GUI Toolkit
# os - provides functions for interacting with operating system
# pickle - primarily used in serializing and deserializing a Python object structure
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os
import pickle


root = tk.Tk()
apps = []
defaultApps = []

# Functions
# Function to add app to apps list
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Opening file window to select the .exe or *.* files
    fileName = filedialog.askopenfilename(initialdir='/', title='Select File',
    filetypes=(('executables','.exe'), ('all files', '*.*')))
    # Appending the selected paths to apps list
    apps.append(fileName)

    # Displaying path to the selected apps
    for app in apps:
        label = tk.Label(frame, text=app,bg='black', fg='green', font=35)
        label.pack()

# Function to open the selected app
def runApps(array):
    if(len(array) == 0):
        # Displaying error to select the path for app to be open
        label = tk.Label(frame, text="ERROR: First Open File", bg='black', fg='red', font=35)
        label.pack()
    else:
        # Running the selected app
        for app in array:
            os.startfile(app)
            print(app)
        
        label = tk.Label(frame, text="Running Apps", bg='black', fg='green', font=35)
        label.pack()

# Function to set default apps 
def setDefault():
    if(len(apps) == 0):
        # Error to select the file
        label = tk.Label(frame, text="ERROR: First Open File", bg='black', fg='red', font=35)
        label.pack()
    else:
        # Appending the selected paths to defaultApps list
        for app in apps:
            defaultApps.append(app)
        
        # saving defaultApps list to systems memory
        pickle.dump(defaultApps, open('defaultApps.dat', 'wb'))

        label = tk.Label(frame, text="Default App Saved", bg='black', fg='green', font=35)
        label.pack()

# Function to run Default apps
def runDefault():
    # loading previously saved file to saveApps variable
    saveApps = pickle.load(open('defaultApps.dat', 'rb'))
    if(len(saveApps) == 0):
        # Error for setting default file
        label = tk.Label(frame, text="ERROR: Set default apps", bg='black', fg='green', font=35)
        label.pack()
    else:
        # Calling runApps for saveApps(default Apps)
        runApps(saveApps)

# GUI
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

# GUI - console for displaying commands
frame = tk.Frame(root, bg='black')
frame.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

#GUI - buttons
btnArea = tk.Frame(root, bg='#415558')
btnArea.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.7)

openFileBtn = tk.Button(btnArea, text="Open File", padx=10, pady=5, fg='#263D42', bg='white', command=addApp)
setDefaultBtn = tk.Button(btnArea, text="Set Default", padx=10, pady=5, fg='#263D42', bg='white', command=setDefault)
runDefaultBtn = tk.Button(btnArea, text="run Default", padx=10, pady=5, fg='#263D42', bg='white', command=runDefault)
runAppsBtn = tk.Button(btnArea, text="Run Apps", padx=10, pady=5, fg='#263D42', bg='white', command=lambda: runApps(apps))

openFileBtn.pack()
runAppsBtn.pack()
setDefaultBtn.pack()
runDefaultBtn.pack()

root.mainloop()