import tools
from videos import queue_videos
print("---Adonis AI Embed---")
def process():
    queue_videos()
    return None

do_videos_refresh = tools.ask_to_bool("Refresh videos?")
do_books_refresh = tools.ask_to_bool("Refresh books?")
do_embed = tools.ask_to_bool("Embed queued?")
do_upload = tools.ask_to_bool("Upload embeded?")
do_batch = tools.ask_to_bool("Individually process queued or batch?")

process()
