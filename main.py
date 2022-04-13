import os
from dataclasses import dataclass
import tkinter as tk

root = tk.Tk()


@dataclass(frozen=True)
class GitIrDownloader:
    base_url: str

    def __post_init__(self):
        os.system(f'wget -nc -c -i {self.base_url}')


if __name__ == "__main__":
    # GitIrDownloader(
    #     'https://git.ir/media/download-links/linkedin-learning-the-python-3-standard-library'
    #     '-86fa4a7a166e4cc39564a3923111eb3d.txt'
    #     )
    root.mainloop()
