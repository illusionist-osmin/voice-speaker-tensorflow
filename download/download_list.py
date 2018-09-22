import os
from download_youtube import DownloadYoutube

if __name__ == "__main__":
    try:
        print("Start Downloading")
        with open("urlList.txt", "r") as f:
            urls=f.readlines()

        for url in urls:
            DownloadYoutube(url)
        print("\nDone!")
    except Exception as e:
        print(e)
