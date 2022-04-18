import os
from dataclasses import dataclass
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()


def open_file():
    file = filedialog.askopenfilename(initialdir='~', title="Open file containing links")
    print(file)


def perform_download():
    print('download file')


canvas = tk.Canvas(root, height=200, width=400, bg='#222222')
canvas.pack()

# frame = tk.Frame(root, bg='#222')
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(root, text='Select File', fg='#fff', bg='#12488B', command=open_file)
open_file.pack()

download = tk.Button(root, text='Download', fg='#fff', bg='#12488B', command=perform_download)
download.pack()


class GitIrDownloader(tk.Frame):
    pass


if __name__ == "__main__":
    root.mainloop()

# @dataclass(frozen=True)
# class GitIrDownloader:
#     base_url: str
#
#     def __post_init__(self):
#         os.system(f'wget -nc -c -i {self.base_url}')

# GitIrDownloader(
#     'https://git.ir/media/download-links/linkedin-learning-the-python-3-standard-library'
#     '-86fa4a7a166e4cc39564a3923111eb3d.txt'
#     )
