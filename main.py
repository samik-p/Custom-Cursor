import ctypes
import os


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

# get path to cursor pack

# open the Install.inf

# read the settings

# set each part of the custom cursor to the cursor pack
