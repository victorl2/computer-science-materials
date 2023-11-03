# Course Downloader
The `download.py` script is designed to automatically download the course lectures and generate a metadata text file. It reads JSON files containing course details and lecture information from a folder named [/courses](/resources/courses/) and downloads the YouTube videos specified in each JSON file. It creates a folder for each course and saves all related videos and metadata there.

## Installation/Usage
You need to have those installed on your machine before running the script:
+ [**Python 3.x**](https://www.python.org/)
+ [**chocolatey**](https://chocolatey.org/) (windows) or [**brew**](https://formulae.brew.sh/) (macos/linux)


To install **ffmpeg** you can use chocolatey on windows:
```
choco install ffmpeg
```

or brew on **macos/linux:**
```
brew install ffmpeg
```

To install the required **Python libraries**, run the following command:
```bash
pip install requests pytube yt_dlp
```

## How to Use

Run the `download.py` script:

```bash
python download.py
```

The script will create a new folder for each course named after the course title.
Download all lectures from YouTube into the course folder.
Generate a metadata.txt file in the course folder with details like the course ID, professors, and source.


# Improve 

```
pip install numpy moviepy opencv-python noisereduce torch torchvision
```