import subprocess
import json
from local_db import local_db
def get_video_urls(channel_url):
    try:
        # Use yt-dlp with the --flat-playlist option to list video URLs
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--dump-json", channel_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Parse the JSON output
        video_urls = []
        for line in result.stdout.strip().split("\n"):
            video_data = json.loads(line)
            if 'url' in video_data:
                video_url = video_data['title']
                # Filter out Shorts URLs
                if "/shorts/" not in video_url:
                    video_urls.append(video_url)

        return video_urls

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
        return []

def queue_videos():
    with open('yt-channels.json', 'r') as file:
        channels = json.load(file)
        for channel_url in channels:
            video_list = get_video_urls(channel_url)
            print(video_list)
def process_queued_videos():
    output = local_db.execute("SELECT * FROM list");
    print(output)
