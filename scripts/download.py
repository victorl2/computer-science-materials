import os
import json
import requests
from pytube import YouTube
import yt_dlp
import glob

output_dir_courses = "../downloads/courses/"
output_dir_papers = "../downloads/papers/"

def download_with_pytube(video_url, output_path, filename):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=output_path, filename=filename + ".mp4")
        return True
    except Exception as e:
        return False

def download_with_yt_dlp(video_url, output_path, filename):
    try:
        ydl_opts = {
            'quiet': True,
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(output_path, f'{filename}.mp4'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return True
    except Exception as e:
        print(f"Failed to download with yt_dlp. Error: {e}")
        return False


# Function to convert arXiv abstract URL to PDF URL
def convert_to_pdf_url(arxiv_url):
    return arxiv_url.replace("abs", "pdf") + ".pdf"

# Loop through each JSON file in the /courses directory
for json_file in glob.glob("../resources/courses/*.json"):
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir_courses):
        os.mkdir(output_dir_courses)

    # Create folder with the course title if it doesn't exist
    course_title = data["course_details"]["title"]
    print(f"# Downloading course: {course_title}")

    course_output_dir = os.path.join(output_dir_courses, course_title)
    if not os.path.exists(course_output_dir):
        os.mkdir(course_output_dir)

    # Generate metadata .txt file
    with open(f"{course_output_dir}/metadata.txt", "w") as f:
        for key, value in data["course_details"].items():
            f.write(f"{key}: {value}\n")
    
    # Download lectures
    for lecture in data["lectures"]:
        lecture_number = lecture["number"]
        lecture_desc = lecture["description"]
        video_url = lecture["video_url"]
        video_filename = f"Lecture_{lecture_number}"
        full_video_path = os.path.join(output_dir_courses, course_title, video_filename + ".mp4")
        
        if os.path.exists(full_video_path):
            continue # Skipping video already exists.

        # Download the video
        print(f"Downloading lecture {lecture_number}: {lecture_desc} from {video_url}")

        # Try downloading with pytube first
        success = download_with_pytube(video_url, course_output_dir, video_filename)
        if(not success):
            download_with_yt_dlp(video_url, course_output_dir, video_filename)

# Loop through each JSON file in the /papers directory
papers_path = os.path.join(output_dir_papers)
if not os.path.exists(papers_path):
    os.mkdir(papers_path)

for paper_file in glob.glob(os.path.join("../resources/papers/*.json")):
    with open(paper_file, 'r') as f:
        paper_data = json.load(f)
    
    paper_title = paper_data['title']
    paper_url = convert_to_pdf_url(paper_data['paper_url'])  # Convert to PDF URL
    paper_filename = f"{paper_title}.pdf".replace("/", "-").replace(" ", "_")
    full_paper_path = os.path.join(papers_path, paper_filename)

    # Check if the paper already exists
    if os.path.exists(full_paper_path):
        print(f"Skipping {paper_filename}, already exists.")
        continue

    print(f"Downloading paper: {paper_title}")

    try:
        response = requests.get(paper_url, stream=True)
        if response.status_code == 200:
            with open(full_paper_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
    except Exception as e:
        print(f"Failed to download {paper_url}. Error: {e}")

print("Download complete. All content is available in the /downloads directory.")