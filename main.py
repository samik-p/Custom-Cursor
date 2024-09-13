import ctypes
import os
import tkinter as tk
from tkinter import filedialog


# Microsoft constants
# https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setsystemcursor
OCR_NORMAL = 32512  # normal select
OCR_APPSTARTING = 32650  # working in background
OCR_WAIT = 32514  # busy
OCR_CROSS = 32515  # precision select
OCR_IBEAM = 32513  # text select
OCR_NO = 32648  # unavailable
OCR_SIZENWSE = 32642  # diagonal resize 1
OCR_SIZENESW = 32643  # diagonal resize 2
OCR_SIZEWE = 32644  # horizontal resize
OCR_SIZENS = 32645  # vertical resize
OCR_SIZEALL = 32646  # move
OCR_UP = 32516  # alternate select
OCR_HAND = 32649  # link select

########
# Set up tkinter application window
########

folder_path = None


def select_folder():
    # open folder selection dialog
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        label.config(text=f"Selected Folder: {folder_path}")


# create main application window
root = tk.Tk()
root.title("Custom Cursor")
root.geometry("600x320")

# create and place button that triggers folder selection
button = tk.Button(root, text="Select Folder", command=select_folder)
button.pack(pady=20)

# label to display the selected folder
label = tk.Label(root, text="No folder selected.")
label.pack(pady=20)

exit = tk.Button(root, text="Set Custom Cursor", command=root.destroy)
exit.pack(pady=20)

# start GUI event loop
root.mainloop()


########
# Set custom cursor
########


def open_folder(path: str):
    files = [
        file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))
    ]


if folder_path:
    print(f"Opening folder {folder_path}")
    open_folder(folder_path)
else:
    print("No folder path specified!")

# get path to cursor pack

# open the Install.inf

# read the settings

# set each part of the custom cursor to the cursor pack
