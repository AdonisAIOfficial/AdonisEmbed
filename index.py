import tools as tools
import json
import csv
print("---Adonis AI Embed---")
def process():
    channels = get_yt_channels_list()
    queue_videos(channels)
    return None
def get_yt_channels_list():
    with open('yt-channels.json', 'r') as f:
        return json.load(f)
def queue_videos(channels):
    with open('queued-videos.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['this is working?'])  # Add the URL as a single row

    print("Queueing")
do_videos_refresh = tools.ask_to_bool("Refresh videos?")
do_books_refresh = tools.ask_to_bool("Refresh books?")
do_embed = tools.ask_to_bool("Embed queued?")
do_upload = tools.ask_to_bool("Upload embeded?")
do_batch = tools.ask_to_bool("Individually process queued or batch?")

process()
