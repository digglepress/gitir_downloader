import os
import urllib.request
from dataclasses import dataclass


@dataclass()
class GitIrDownloader:
    base_url: str

    def __post_init__(self):
        os.chdir('/media/Storage/')
        data = urllib.request.urlopen(self.base_url).read()
        self.file_url = data.decode('utf-8').split("\n")[3]
        file_name = self.file_url.split("/")[4].replace("%20", " ").split("-")[0]
        try:
            os.mkdir(os.path.join(os.curdir, file_name))
        except FileExistsError:
            pass
        os.chdir(os.path.join(os.getcwd(), file_name))

    def download(self):
        os.system(f'wget -nc -c -i {self.base_url}')


file = GitIrDownloader(
    'https://git.ir/media/download-links/udemy-the-ultimate-authentication-course-with-djan'
    '-258d22a936c54232867c0bcd31e3363c.txt'
)

if __name__ == "__main__":
    file.download()
