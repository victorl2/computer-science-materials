# Course Downloader
The download.py script is designed to automatically download course lectures and generate a metadata text file for courses. It reads JSON files containing course details and lecture information from a folder named [/courses](/resources/courses/) and downloads the YouTube videos specified in each JSON file. It creates a folder for each course and saves all related videos and metadata there.

## Dependencies

+ Python 3.x
+ requests
+ pytube

To install the required Python libraries, run the following command:

```bash
pip install requests pytube
```

## How to Use

Run the `download.py` script:

```bash
python download.py
```

The script will:

Create a new folder for each course named after the course title.
Download all lectures from YouTube into the course folder.
Generate a metadata.txt file in the course folder with details like the course ID, professors, and source.

Feel free to add this README to the same directory as your download.py script. This will help anyone using the script understand what it does and how to use it.