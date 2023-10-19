from tiktokapipy.api import TikTokAPI
from tiktokapipy import models
from io import StringIO
import csv

def get_video_stats():
    with TikTokAPI() as api:
        data = []
        # Search for tiktoks with the following tabs
        tags = ["streetwear", "fashion", "styling", "outfit", "ootd"]
        for tag in tags:
            challenge = api.challenge(tag, video_limit=20)
            for video in challenge.videos:

                # Get tiktok user information
                vid = api.video(video.id)
                creator = vid.creator()

                # Collect comment and hashtag information
                try:
                    video.comments._fetch_sync()
                    comments = list(map(lambda x: x.text, video.comments._collected_values))
                except:
                    comments = []
                
                try:
                    hashtags = list(map(lambda x: "#" + x.title, video.challenges))
                except:
                    hashtags = []
                
                # URL, account, views, likes, comments, saved, caption, hashtags, date posted, date collected
                rowData = [
                    models.video.video_link(video.id),
                    creator.nickname,
                    video.stats.play_count,
                    video.stats.digg_count,
                    video.stats.comment_count,
                    comments,
                    video.stats.share_count,
                    video.desc,
                    hashtags,
                    video.create_time
                ]
                data.append(rowData)

        # Produce output to be written into CSV
        output = StringIO()
        writer = csv.writer(output)
        headers = ["Post URL", "Account", "Views", "Likes", "# of Comments", "Comments", "Saved", "Caption", "Hashtags", "Date Posted", "Date Collected"]
        writer.writerow(headers)
        writer.writerows(data)
        print(output.getvalue())

get_video_stats()