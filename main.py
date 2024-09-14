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

settings_dict = {
    OCR_NORMAL: set(["pointer"]),
    OCR_APPSTARTING: set(["work"]),
    OCR_WAIT: set(["busy"]),
    OCR_CROSS: set(["cross"]),
    OCR_IBEAM: set(["text", "pin"]),
    OCR_NO: set(["unavailiable", "unavailable"]),
    OCR_SIZENWSE: set(["dgn1"]),
    OCR_SIZENESW: set(["dgn2"]),
    OCR_SIZEWE: set(["horz"]),
    OCR_SIZENS: set(["vert"]),
    OCR_SIZEALL: set(["move"]),
    OCR_UP: set(["alternate"]),
    OCR_HAND: set(["link"]),
}

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

    if "Install.inf" not in files:
        print("Install.inf file not found")
        exit()

    return os.path.join(path, "Install.inf")


if not folder_path:
    print("No folder path specified!")
    exit()


print(f"Opening folder {folder_path}")
install_fp = open_folder(folder_path)

# open the Install.inf
file = open(install_fp, "r")
if not file:
    print("Install.inf could not be opened!")
    exit()

strings_line_found = False
for line in file:
    if "[Strings]" in line:
        strings_line_found = True
        break

if not strings_line_found:
    print("Could not find [Strings] section of Install.inf")
    file.close()
    exit()

# read the cursor settings
for line in file:
    cur_line = line.strip().split("=")
    if len(cur_line) == 2:
        cur_line[0] = cur_line[0].strip()
        cur_line[1] = cur_line[1].strip().replace('"', "")

    for k in settings_dict:
        if cur_line[0] in settings_dict[k]:
            cursor_path = os.path.join(folder_path, cur_line[1])
            result = ctypes.windll.user32.SetSystemCursor(
                ctypes.windll.user32.LoadCursorFromFileW(cursor_path), k
            )

            if result:
                print(f"[OK] {cur_line[0]}: {cur_line[1]}")
            else:
                print(f"[XX] {cur_line[0]}: Load Failed")

print("Program complete! Exiting")
file.close()
